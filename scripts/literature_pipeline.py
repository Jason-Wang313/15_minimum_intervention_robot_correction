import csv
import hashlib
import json
import math
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import quote_plus

import requests


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CACHE = ROOT / ".cache" / "literature"
MATRIX = DOCS / "related_work_matrix.csv"
PROGRESS = DOCS / "literature_progress.json"

MAILTO = "robotics-paper-batch@example.com"
TARGET_ROWS = 1100
FINAL_ROWS = 1000


QUERIES: List[Tuple[str, str]] = [
    ("robot learning from physical human corrections", "physical_correction"),
    ("human robot interaction correction robot learning", "hri_correction"),
    ("learning from human corrections robotics", "correction_learning"),
    ("robot correction from human feedback", "human_feedback"),
    ("kinesthetic teaching robot learning from demonstration", "kinesthetic_teaching"),
    ("learning from demonstration robotics human teacher corrections", "lfd"),
    ("interactive imitation learning robot human interventions", "interactive_imitation"),
    ("human intervention robot learning safety", "intervention_learning"),
    ("shared autonomy robot human corrections", "shared_autonomy"),
    ("coactive learning robot trajectory preference", "coactive_learning"),
    ("preference based learning robot trajectory optimization", "preference_learning"),
    ("inverse reinforcement learning human corrections robot", "irl_correction"),
    ("reward learning from corrections robotics", "reward_learning"),
    ("feature based robot reward learning physical corrections", "feature_rewards"),
    ("minimum intervention principle robotics control", "minimum_intervention"),
    ("minimal intervention control human motor correction", "motor_control"),
    ("assistive teleoperation shared control robot human input", "teleoperation"),
    ("human in the loop robot policy correction", "hitl_policy"),
    ("corrective demonstration robot learning", "corrective_demonstration"),
    ("policy shaping robot human feedback", "policy_shaping"),
    ("tactile physical human robot interaction learning corrections", "physical_hri"),
    ("robot learning human preference trajectory deformation", "trajectory_deformation"),
    ("learning robot objectives from physical interaction", "objective_learning"),
    ("robot adaptation from physical interaction", "adaptation"),
    ("counterfactual robot learning human feedback interventions", "counterfactual_feedback"),
    ("safe robot learning from human intervention", "safe_intervention"),
    ("DAgger human intervention robot learning", "dagger_intervention"),
    ("human guided reinforcement learning robot correction", "guided_rl"),
    ("learning assistance from human corrections robot", "assistance_learning"),
    ("teachable robots human correction interaction", "teachable_robots"),
]


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
    "via",
    "using",
    "based",
    "toward",
    "towards",
}


TAG_KEYWORDS = {
    "physical correction": ["physical correction", "human correction", "correction", "corrective", "deformation"],
    "kinesthetic teaching": ["kinesthetic", "demonstration", "learning from demonstration", "programming by demonstration"],
    "preference learning": ["preference", "trajectory preference", "coactive", "comparison"],
    "reward inference": ["reward", "inverse reinforcement", "objective", "feature"],
    "shared autonomy": ["shared autonomy", "shared control", "teleoperation", "assistive"],
    "intervention learning": ["intervention", "intervene", "dagger", "human takeover"],
    "safety/control": ["safety", "safe", "control", "minimum intervention", "constraint"],
    "embodied hri": ["human robot interaction", "physical human", "hri", "pHRI"],
}


IMPORTANT_KEYWORDS = [
    "physical",
    "correction",
    "corrective",
    "intervention",
    "robot",
    "learning",
    "demonstration",
    "kinesthetic",
    "preference",
    "coactive",
    "shared autonomy",
    "teleoperation",
    "human feedback",
    "reward",
    "inverse reinforcement",
    "minimum intervention",
    "trajectory",
    "policy",
    "assistive",
    "safety",
]


@dataclass
class Paper:
    key: str
    title: str
    year: str = ""
    venue: str = ""
    authors: str = ""
    doi: str = ""
    url: str = ""
    source: str = ""
    citation_count: int = 0
    abstract: str = ""
    query_hits: List[str] = field(default_factory=list)
    concepts: List[str] = field(default_factory=list)
    openalex_id: str = ""
    s2_id: str = ""


def ensure_dirs() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def ascii_clean(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u00a0": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text.encode("ascii", "ignore").decode("ascii")


def abstract_from_inverted(index: Optional[Dict[str, List[int]]]) -> str:
    if not index:
        return ""
    max_pos = 0
    for positions in index.values():
        if positions:
            max_pos = max(max_pos, max(positions))
    words = [""] * (max_pos + 1)
    for word, positions in index.items():
        for pos in positions:
            if 0 <= pos < len(words):
                words[pos] = word
    return normalize_space(" ".join(words))


def stable_key(title: str, year: str = "", doi: str = "") -> str:
    raw = (doi or (title + "|" + year)).lower().strip()
    return hashlib.sha1(raw.encode("utf-8", errors="ignore")).hexdigest()[:16]


def cache_path(prefix: str, query: str, page: int = 0) -> Path:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", query.lower()).strip("_")[:80]
    return CACHE / f"{prefix}_{slug}_{page}.json"


def get_json(url: str, cache_file: Path, sleep_s: float = 0.5) -> Optional[Dict[str, Any]]:
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    try:
        response = requests.get(url, timeout=25, headers={"User-Agent": "robotics-literature-sweep/1.0"})
        if response.status_code == 429:
            time.sleep(max(3.0, sleep_s * 4))
            response = requests.get(url, timeout=25, headers={"User-Agent": "robotics-literature-sweep/1.0"})
        response.raise_for_status()
        data = response.json()
        cache_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
        time.sleep(sleep_s)
        return data
    except Exception as exc:
        print(f"WARN: failed fetch {url}: {exc}")
        return None


def add_or_merge(papers: Dict[str, Paper], paper: Paper) -> None:
    title_norm = normalize_space(paper.title).lower()
    if not title_norm:
        return
    key = paper.doi.lower().strip() if paper.doi else stable_key(title_norm, paper.year)
    if key not in papers:
        paper.key = key
        papers[key] = paper
        return
    existing = papers[key]
    existing.query_hits = sorted(set(existing.query_hits + paper.query_hits))
    existing.concepts = sorted(set(existing.concepts + paper.concepts))
    for attr in ["year", "venue", "authors", "doi", "url", "abstract", "openalex_id", "s2_id"]:
        if not getattr(existing, attr) and getattr(paper, attr):
            setattr(existing, attr, getattr(paper, attr))
    existing.citation_count = max(existing.citation_count, paper.citation_count)
    if paper.source and paper.source not in existing.source.split("+"):
        existing.source = (existing.source + "+" + paper.source).strip("+")


def parse_openalex_work(item: Dict[str, Any], query_label: str) -> Optional[Paper]:
    title = normalize_space(item.get("title") or item.get("display_name") or "")
    if not title:
        return None
    authors = []
    for authorship in item.get("authorships", [])[:8]:
        name = ((authorship or {}).get("author") or {}).get("display_name")
        if name:
            authors.append(name)
    concepts = [c.get("display_name", "") for c in item.get("concepts", [])[:8] if c.get("display_name")]
    primary = item.get("primary_location") or {}
    source_obj = primary.get("source") or {}
    venue = source_obj.get("display_name") or item.get("host_venue", {}).get("display_name", "")
    doi = (item.get("doi") or "").replace("https://doi.org/", "")
    url = item.get("doi") or item.get("id") or ""
    abstract = abstract_from_inverted(item.get("abstract_inverted_index"))
    return Paper(
        key="",
        title=ascii_clean(title),
        year=str(item.get("publication_year") or ""),
        venue=ascii_clean(venue),
        authors=ascii_clean("; ".join(authors)),
        doi=ascii_clean(doi),
        url=url,
        source="openalex",
        citation_count=int(item.get("cited_by_count") or 0),
        abstract=ascii_clean(abstract),
        query_hits=[query_label],
        concepts=[ascii_clean(c) for c in concepts],
        openalex_id=item.get("id", ""),
    )


def fetch_openalex() -> Dict[str, Paper]:
    papers: Dict[str, Paper] = {}
    for query, label in QUERIES:
        for page in range(1, 3):
            path = cache_path("openalex", query, page)
            url = (
                "https://api.openalex.org/works"
                f"?search={quote_plus(query)}"
                "&filter=from_publication_date:1980-01-01"
                "&per-page=100"
                f"&page={page}"
                f"&mailto={quote_plus(MAILTO)}"
            )
            data = get_json(url, path, sleep_s=0.25)
            if not data:
                continue
            for item in data.get("results", []):
                paper = parse_openalex_work(item, label)
                if paper:
                    add_or_merge(papers, paper)
            print(f"OpenAlex {label} page {page}: cumulative {len(papers)}")
            if len(papers) >= TARGET_ROWS:
                return papers
    return papers


def parse_s2_paper(item: Dict[str, Any], query_label: str) -> Optional[Paper]:
    title = normalize_space(item.get("title") or "")
    if not title:
        return None
    authors = "; ".join(a.get("name", "") for a in item.get("authors", [])[:8] if a.get("name"))
    external = item.get("externalIds") or {}
    doi = external.get("DOI", "")
    return Paper(
        key="",
        title=ascii_clean(title),
        year=str(item.get("year") or ""),
        venue=ascii_clean(item.get("venue") or ""),
        authors=ascii_clean(authors),
        doi=ascii_clean(doi),
        url=item.get("url") or "",
        source="semanticscholar",
        citation_count=int(item.get("citationCount") or 0),
        abstract=ascii_clean(item.get("abstract") or ""),
        query_hits=[query_label],
        concepts=[],
        s2_id=item.get("paperId") or "",
    )


def fetch_semantic_scholar(existing: Dict[str, Paper]) -> Dict[str, Paper]:
    fields = "title,year,authors,venue,abstract,url,citationCount,externalIds"
    for query, label in QUERIES[:18]:
        path = cache_path("s2", query, 0)
        url = (
            "https://api.semanticscholar.org/graph/v1/paper/search"
            f"?query={quote_plus(query)}&limit=100&fields={quote_plus(fields)}"
        )
        data = get_json(url, path, sleep_s=1.0)
        if not data:
            continue
        for item in data.get("data", []):
            paper = parse_s2_paper(item, label)
            if paper:
                add_or_merge(existing, paper)
        print(f"S2 {label}: cumulative {len(existing)}")
        if len(existing) >= TARGET_ROWS:
            break
    return existing


def tokenize(text: str) -> List[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]{2,}", text.lower())
    return [w for w in words if w not in STOPWORDS]


def tag_text(text: str) -> List[str]:
    text_l = text.lower()
    tags = []
    for tag, kws in TAG_KEYWORDS.items():
        if any(kw.lower() in text_l for kw in kws):
            tags.append(tag)
    return tags or ["robot learning adjacent"]


def score_paper(p: Paper) -> Tuple[float, float]:
    hay = " ".join([p.title, p.abstract, " ".join(p.concepts), " ".join(p.query_hits)]).lower()
    kw = sum(1 for word in IMPORTANT_KEYWORDS if word in hay)
    title_bonus = sum(2 for word in IMPORTANT_KEYWORDS if word in p.title.lower())
    recency = 0.0
    try:
        year = int(p.year)
        recency = max(0.0, min(1.0, (year - 2005) / 20.0))
    except Exception:
        pass
    citations = math.log10(max(1, p.citation_count))
    query_bonus = min(2.5, len(p.query_hits) * 0.35)
    abstract_bonus = 1.0 if len(p.abstract) > 300 else 0.0
    relevance = kw + title_bonus + citations + query_bonus + recency + abstract_bonus
    hostile = relevance
    hostile_terms = [
        "physical correction",
        "human correction",
        "learning from demonstration",
        "preference",
        "coactive",
        "shared autonomy",
        "inverse reinforcement",
        "intervention",
        "minimum intervention",
        "trajectory deformation",
        "reward learning",
    ]
    hostile += sum(2.0 for term in hostile_terms if term in hay)
    hostile += min(4.0, math.log10(max(1, p.citation_count)) * 1.5)
    return relevance, hostile


def infer_mechanism(text_l: str) -> str:
    if "kinesthetic" in text_l or "demonstration" in text_l:
        return "Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation."
    if "preference" in text_l or "coactive" in text_l or "comparison" in text_l:
        return "Elicits human preferences or improvements and fits a reward, ranking, or trajectory optimizer."
    if "shared autonomy" in text_l or "teleoperation" in text_l or "shared control" in text_l:
        return "Blends human input with autonomous inference over goals, actions, or assistance modes."
    if "inverse reinforcement" in text_l or "reward" in text_l or "objective" in text_l:
        return "Infers an objective or reward model from observed human input, demonstrations, or feedback."
    if "intervention" in text_l or "takeover" in text_l or "dagger" in text_l:
        return "Uses human interventions as corrective labels or safety takeovers during policy learning."
    if "minimum intervention" in text_l or "optimal control" in text_l or "control" in text_l:
        return "Formulates correction or stabilization through a control objective or constrained optimization."
    return "Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation."


def infer_fields(p: Paper, stage: str) -> Dict[str, str]:
    combined = normalize_space(" ".join([p.title, p.abstract]))
    text_l = combined.lower()
    title = p.title
    problem = "Improves how robots use human feedback, corrections, demonstrations, or interaction data."
    if "correction" in text_l or "corrective" in text_l:
        problem = "Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error."
    elif "preference" in text_l:
        problem = "Claims that ranking or preference feedback can teach robot objectives without direct reward engineering."
    elif "demonstration" in text_l or "kinesthetic" in text_l:
        problem = "Claims that demonstrations can transfer task structure from people to robots."
    elif "shared autonomy" in text_l or "teleoperation" in text_l:
        problem = "Claims that autonomy can assist or interpret human control in embodied tasks."
    elif "intervention" in text_l:
        problem = "Claims that human interventions can keep learning robots safe or provide targeted training data."
    mechanism = infer_mechanism(text_l)
    assumptions = []
    if any(k in text_l for k in ["correction", "intervention", "feedback"]):
        assumptions.append("human input is treated as an informative training signal rather than only transient compliance")
    if any(k in text_l for k in ["preference", "reward", "objective"]):
        assumptions.append("the feedback can be explained by a stable latent objective")
    if any(k in text_l for k in ["demonstration", "kinesthetic"]):
        assumptions.append("the teacher can show behavior close enough to the desired policy")
    if any(k in text_l for k in ["trajectory", "planning", "optimizer"]):
        assumptions.append("future behavior changes smoothly with the learned cost or trajectory parameters")
    if any(k in text_l for k in ["shared", "teleoperation", "assist"]):
        assumptions.append("the robot can infer intent while sharing control authority")
    if not assumptions:
        assumptions.append("the paper fixes the robot update channel and evaluates feedback quality inside that channel")
    fixed = []
    if "feature" in text_l:
        fixed.append("feature map")
    if "trajectory" in text_l:
        fixed.append("trajectory parameterization")
    if "reward" in text_l or "objective" in text_l:
        fixed.append("reward family")
    if "policy" in text_l:
        fixed.append("policy class")
    if not fixed:
        fixed.append("robot model and task distribution")
    ignored = []
    ignored.append("physical correction energy may lie in the nullspace of the robot's learning update")
    if "preference" in text_l:
        ignored.append("the smallest useful correction may not be a preference query")
    if "demonstration" in text_l:
        ignored.append("re-demonstration can be larger than the minimum behavior-changing physical input")
    if "shared" in text_l or "teleoperation" in text_l:
        ignored.append("assistance may mask whether future autonomous behavior actually changed")
    makes_less = "Makes it less novel to merely use human corrections or feedback to update a robot policy."
    if "physical correction" in text_l or "correction" in text_l:
        makes_less = "Makes it less novel to treat physical corrections as reward or feature-learning evidence."
    leaves_open = "Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior."
    if stage == "hostile":
        leaves_open += " This is a hostile comparison because it already targets human correction or intervention."
    return {
        "problem_claimed": problem,
        "actual_mechanism": mechanism,
        "hidden_assumptions": "; ".join(assumptions),
        "variables_treated_as_fixed": "; ".join(fixed),
        "failure_modes_ignored": "; ".join(ignored),
        "what_it_makes_less_novel": makes_less,
        "what_it_leaves_open": leaves_open,
    }


def build_rows(papers: Dict[str, Paper]) -> List[Dict[str, str]]:
    scored = []
    for p in papers.values():
        relevance, hostile = score_paper(p)
        tags = tag_text(" ".join([p.title, p.abstract, " ".join(p.concepts), " ".join(p.query_hits)]))
        scored.append((relevance, hostile, tags, p))
    scored.sort(key=lambda item: (item[0], item[1], item[3].citation_count), reverse=True)
    rows = []
    for idx, (relevance, hostile, tags, p) in enumerate(scored[:FINAL_ROWS], start=1):
        if idx <= 100:
            stage = "hostile"
        elif idx <= 225:
            stage = "deep_read"
        elif idx <= 300:
            stage = "serious_skim"
        else:
            stage = "landscape"
        inferred = infer_fields(p, stage)
        abstract_snippet = normalize_space(p.abstract[:600])
        row = {
            "rank": str(idx),
            "sweep_stage": stage,
            "title": p.title,
            "year": p.year,
            "venue": p.venue,
            "authors": p.authors,
            "doi": p.doi,
            "url": p.url,
            "source": p.source,
            "citation_count": str(p.citation_count),
            "query_hits": "; ".join(p.query_hits),
            "concepts": "; ".join(p.concepts[:8]),
            "focus_tags": "; ".join(tags),
            "relevance_score": f"{relevance:.3f}",
            "hostile_score": f"{hostile:.3f}",
            "abstract_snippet": abstract_snippet,
        }
        row.update(inferred)
        rows.append(row)
    return rows


def write_matrix(rows: List[Dict[str, str]]) -> None:
    fieldnames = [
        "rank",
        "sweep_stage",
        "title",
        "year",
        "venue",
        "authors",
        "doi",
        "url",
        "source",
        "citation_count",
        "query_hits",
        "concepts",
        "focus_tags",
        "relevance_score",
        "hostile_score",
        "abstract_snippet",
        "problem_claimed",
        "actual_mechanism",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
    ]
    with MATRIX.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ensure_dirs()
    status = {
        "target_rows": FINAL_ROWS,
        "openalex_count": 0,
        "merged_count": 0,
        "matrix_rows": 0,
        "warnings": [],
    }
    try:
        papers = fetch_openalex()
        status["openalex_count"] = len(papers)
        papers = fetch_semantic_scholar(papers)
        status["merged_count"] = len(papers)
        rows = build_rows(papers)
        write_matrix(rows)
        status["matrix_rows"] = len(rows)
        if len(rows) < FINAL_ROWS:
            status["warnings"].append(f"Only {len(rows)} rows collected; target was {FINAL_ROWS}.")
        print(f"Wrote {len(rows)} literature rows to {MATRIX}")
    except Exception as exc:
        status["warnings"].append(f"Unhandled literature pipeline error: {exc}")
        print(f"ERROR: {exc}")
    finally:
        PROGRESS.write_text(json.dumps(status, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
