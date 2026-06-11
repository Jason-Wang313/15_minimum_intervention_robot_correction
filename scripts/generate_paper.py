import json
import math
import shutil
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
DOCS = ROOT / "docs"
FIGURES = ROOT / "figures"
EXPERIMENTS = ROOT / "experiments"


THESIS = (
    "The smallest useful physical robot correction is not the smallest displacement "
    "that fixes the current motion; it is the minimum-energy correction whose image "
    "through the robot's update channel crosses a future-behavior decision boundary."
)


def load_summary() -> Dict[str, Dict[str, float]]:
    path = EXPERIMENTS / "summary.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def pct(summary: Dict[str, Dict[str, float]], method: str, key: str) -> str:
    try:
        return f"{100.0 * summary[method][key]:.1f}"
    except Exception:
        return "--"


def num(summary: Dict[str, Dict[str, float]], method: str, key: str) -> str:
    try:
        value = summary[method][key]
        if not math.isfinite(value):
            return "--"
        return f"{value:.3f}"
    except Exception:
        return "--"


def copy_figures() -> None:
    target = PAPER / "figures"
    target.mkdir(parents=True, exist_ok=True)
    for name in ["success_rates.png", "correction_norms.png"]:
        src = FIGURES / name
        if src.exists():
            shutil.copyfile(src, target / name)


def write_bib() -> None:
    bib = r"""
@article{argall2009survey,
  title={A survey of robot learning from demonstration},
  author={Argall, Brenna D. and Chernova, Sonia and Veloso, Manuela and Browning, Brett},
  journal={Robotics and Autonomous Systems},
  volume={57},
  number={5},
  pages={469--483},
  year={2009}
}

@inproceedings{akgun2012keyframe,
  title={Keyframe-based learning from demonstration},
  author={Akgun, Baris and Cakmak, Maya and Yoo, Jae Wook and Thomaz, Andrea L.},
  booktitle={International Journal of Social Robotics},
  year={2012}
}

@article{chernova2014robot,
  title={Robot learning from human teachers},
  author={Chernova, Sonia and Thomaz, Andrea L.},
  journal={Synthesis Lectures on Artificial Intelligence and Machine Learning},
  volume={8},
  number={3},
  pages={1--121},
  year={2014}
}

@inproceedings{jain2015learning,
  title={Learning trajectory preferences for manipulators via iterative improvement},
  author={Jain, Ashesh and Sharma, Shikhar and Joachims, Thorsten and Saxena, Ashutosh},
  booktitle={Advances in Neural Information Processing Systems},
  year={2013}
}

@inproceedings{bajcsy2017learning,
  title={Learning from physical human corrections, one feature at a time},
  author={Bajcsy, Andrea and Losey, Dylan P. and O'Malley, Marcia K. and Dragan, Anca D.},
  booktitle={ACM/IEEE International Conference on Human-Robot Interaction},
  year={2017}
}

@inproceedings{bajcsy2018learning,
  title={Learning robot objectives from physical human interaction},
  author={Bajcsy, Andrea and Losey, Dylan P. and O'Malley, Marcia K. and Dragan, Anca D.},
  booktitle={Conference on Robot Learning},
  year={2017}
}

@inproceedings{bobu2020feature,
  title={Feature expansive reward learning: Rethinking human input},
  author={Bobu, Andreea and Wiggert, Matthew and Tomlin, Claire and Dragan, Anca D.},
  booktitle={ACM/IEEE International Conference on Human-Robot Interaction},
  year={2021}
}

@inproceedings{dragan2013legibility,
  title={Generating legible motion},
  author={Dragan, Anca D. and Lee, Kenton C. T. and Srinivasa, Siddhartha S.},
  booktitle={Robotics: Science and Systems},
  year={2013}
}

@inproceedings{javdani2015shared,
  title={Shared autonomy via hindsight optimization},
  author={Javdani, Shervin and Srinivasa, Siddhartha S. and Bagnell, J. Andrew},
  booktitle={Robotics: Science and Systems},
  year={2015}
}

@article{losey2018review,
  title={A review of intent detection, arbitration, and communication aspects of shared control for physical human-robot interaction},
  author={Losey, Dylan P. and McDonald, Craig G. and Battaglia, Edoardo and O'Malley, Marcia K.},
  journal={Applied Mechanics Reviews},
  volume={70},
  number={1},
  year={2018}
}

@inproceedings{sadigh2017active,
  title={Active preference-based learning of reward functions},
  author={Sadigh, Dorsa and Dragan, Anca D. and Sastry, S. Shankar and Seshia, Sanjit A.},
  booktitle={Robotics: Science and Systems},
  year={2017}
}

@article{wirth2017survey,
  title={A survey of preference-based reinforcement learning methods},
  author={Wirth, Christian and Akrour, Riad and Neumann, Gerhard and F{\"u}rnkranz, Johannes},
  journal={Journal of Machine Learning Research},
  volume={18},
  number={136},
  pages={1--46},
  year={2017}
}

@inproceedings{ross2011dagger,
  title={A reduction of imitation learning and structured prediction to no-regret online learning},
  author={Ross, Stephane and Gordon, Geoffrey and Bagnell, Drew},
  booktitle={International Conference on Artificial Intelligence and Statistics},
  year={2011}
}

@inproceedings{kelly2019hgdagger,
  title={HG-DAgger: Interactive imitation learning with human experts},
  author={Kelly, Michael and Sidrane, Chelsea and Driggs-Campbell, Katherine and Kochenderfer, Mykel J.},
  booktitle={International Conference on Robotics and Automation},
  year={2019}
}

@inproceedings{christiano2017deep,
  title={Deep reinforcement learning from human preferences},
  author={Christiano, Paul F. and Leike, Jan and Brown, Tom B. and Martic, Miljan and Legg, Shane and Amodei, Dario},
  booktitle={Advances in Neural Information Processing Systems},
  year={2017}
}

@inproceedings{hadfieldmenell2016cirL,
  title={Cooperative inverse reinforcement learning},
  author={Hadfield-Menell, Dylan and Russell, Stuart J. and Abbeel, Pieter and Dragan, Anca D.},
  booktitle={Advances in Neural Information Processing Systems},
  year={2016}
}

@inproceedings{fisac2017pragmatic,
  title={Pragmatic-pedagogic value alignment},
  author={Fisac, Jaime F. and Gates, Monica A. and Hamrick, Jessica B. and Liu, Chang and Hadfield-Menell, Dylan and Palaniappan, Meera and Malik, Dhruv and Sastry, S. Shankar and Griffiths, Thomas L. and Dragan, Anca D.},
  booktitle={Robotics Research},
  year={2017}
}

@article{todorov2004optimality,
  title={Optimality principles in sensorimotor control},
  author={Todorov, Emanuel},
  journal={Nature Neuroscience},
  volume={7},
  number={9},
  pages={907--915},
  year={2004}
}

@article{knox2009interactively,
  title={Interactively shaping agents via human reinforcement: The TAMER framework},
  author={Knox, W. Bradley and Stone, Peter},
  journal={International Conference on Knowledge Capture},
  year={2009}
}
""".strip()
    (PAPER / "references.bib").write_text(bib + "\n", encoding="utf-8")


def result_table(summary: Dict[str, Dict[str, float]]) -> str:
    rows = []
    for label, method in [
        ("UBC (ours)", "UBC"),
        ("Current-only", "current_only"),
        ("Single-axis current", "one_axis_current"),
        ("Gradient line search", "gradient_line_search"),
        ("Random search", "random_search"),
    ]:
        rows.append(
            f"{label} & {pct(summary, method, 'future_success_reachable')} & "
            f"{pct(summary, method, 'detects_unreachable')} & "
            f"{num(summary, method, 'mean_norm_successful')} \\\\"
        )
    return "\n".join(rows)


def write_tex() -> None:
    summary = load_summary()
    PAPER.mkdir(parents=True, exist_ok=True)
    copy_figures()
    table = result_table(summary)
    tex = rf"""
\documentclass{{article}}
\usepackage{{iclr2026_conference,times}}
\usepackage{{hyperref}}
\usepackage{{url}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{amsthm}}
\usepackage{{microtype}}

\title{{Minimum Effective Corrections for Future Robot Behavior}}

\author{{Anonymous Authors}}

\newtheorem{{proposition}}{{Proposition}}
\newtheorem{{definition}}{{Definition}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Physical corrections are a natural way to teach robots, but a correction that repairs the current execution can still be invisible to the learner that determines future behavior. We formalize a \emph{{Minimum Effective Correction}}: the smallest physical intervention whose image through the robot's update rule crosses a specified future-behavior boundary. The resulting mechanism, Update-Boundary Correction (UBC), solves a local minimum-norm halfspace problem and returns either a correction, a nullspace warning, or an infeasibility certificate for the robot's current correction channel. In a controlled embodied-correction simulator, UBC succeeds on reachable future-behavior constraints while current-only corrections often repair the immediate margin without changing future behavior. The claims are intentionally local: the paper proves the certificate for affine update linearizations and reports simulated evidence, not a global or hardware guarantee.
\end{{abstract}}

\section{{Introduction}}
Robots are often corrected physically: a person nudges a manipulator away from an obstacle, guides a waypoint through a safer passage, or takes over a shared-control interface. Prior work shows that such feedback can teach demonstrations, rewards, preferences, and policies \citep{{argall2009survey,chernova2014robot,bajcsy2017learning,sadigh2017active,ross2011dagger,kelly2019hgdagger}}. Yet these methods usually ask what the human meant, not whether the physical input lies in a part of the robot update map that can change future autonomous behavior.

This distinction matters because robot correction has two faces. One face is immediate compliance: the robot's current motion changes because a human applied force or selected an alternative command. The other is learning: future trajectories change after the contact ends. These can disagree. A small push can fix the present motion while falling in the learner's nullspace; a larger but differently directed correction can be the true minimum that changes future behavior.

This paper studies the object suggested by that disagreement. Given a robot learner, a correction interface, and a finite set of future behavior predicates, what is the smallest physical correction that changes the future policy? The answer is not generally the smallest geometric trajectory deformation. It is the smallest correction after projection through the robot's update channel.

\textbf{{Contributions.}} We make three contributions. First, we define the Minimum Effective Correction (MEC), a learner-relative object that distinguishes behavior-changing corrections from compliance-only motion. Second, we derive Update-Boundary Correction (UBC), a local convex certificate for affine update models and linearized future-behavior margins. Third, we provide runnable evidence showing that immediate repair can fail to produce future behavior change, while UBC either finds the minimum correction in the reachable channel or declares the request unreachable.

\section{{Related Work}}
\textbf{{Learning from demonstration and correction.}} Learning from demonstration converts human traces into policies or trajectory models \citep{{argall2009survey,akgun2012keyframe,chernova2014robot}}. Physical correction methods go further by treating corrective interaction as information about missing reward features or desired behavior \citep{{bajcsy2017learning,bajcsy2018learning,bobu2020feature}}. Our work does not claim novelty in using corrections as feedback. Instead, it asks whether a physical correction is effective under the learner's own update channel.

\textbf{{Preferences and coactive improvement.}} Preference-based and coactive methods use comparisons or improvements to infer reward functions \citep{{jain2015learning,sadigh2017active,wirth2017survey,christiano2017deep}}. They reduce the burden of full demonstrations, but the feedback object is usually a label or ranking. MEC is different: the optimization variable is the physical intervention itself, with cost measured before the learner projects it into parameter space.

\textbf{{Shared autonomy and intervention-aided learning.}} Shared autonomy blends human commands with autonomous inference \citep{{javdani2015shared,losey2018review}}. Intervention-aided imitation learning treats takeovers as corrective data \citep{{ross2011dagger,kelly2019hgdagger}}. These settings reveal the same risk: successful assistance or safe takeover does not prove that future autonomous behavior has changed. UBC targets that gap directly.

\textbf{{Minimum intervention.}} The minimum intervention principle in motor control emphasizes corrections only along task-relevant dimensions \citep{{todorov2004optimality}}. We borrow the spirit but change the object: the relevant dimensions are not only task-state dimensions, but the image of the robot's learning update map.

\section{{Minimum Effective Correction}}
Let $\theta \in \mathbb{{R}}^p$ denote the robot learner state, such as reward weights, planner parameters, or policy features. A physical correction $c \in \mathbb{{R}}^d$ is applied during an interaction $\tau$. The robot update is
\begin{{equation}}
    \theta^+ = U(\theta,\tau,c).
\end{{equation}}
For future contexts $z_j$, define behavior margins $m_j(\theta^+)$. The desired future behavior is certified when $m_j(\theta^+) \geq \gamma$ for all $j$ in a finite set $\mathcal{{Z}}$.

\begin{{definition}}[Minimum Effective Correction]
Given a correction cost matrix $W \succ 0$, the Minimum Effective Correction is
\begin{{equation}}
    c^\star = \arg\min_c \|c\|_W^2
    \quad \textrm{{s.t.}} \quad
    m_j(U(\theta,\tau,c)) \geq \gamma, \quad \forall z_j \in \mathcal{{Z}}.
\end{{equation}}
If no feasible $c$ exists inside the physical correction channel, the learner cannot certify the requested future behavior from this interface at this state.
\end{{definition}}

The definition is intentionally learner-relative. It does not say that the task is impossible, that the human is wrong, or that no other teaching interface would work. It says only that the current robot update map cannot turn this kind of physical correction into the requested future behavior.

\section{{Update-Boundary Correction}}
UBC solves the local version of MEC. Linearize the update around $c=0$:
\begin{{equation}}
    U(\theta,\tau,c) \approx \theta + Jc,
\end{{equation}}
where $J = \partial U / \partial c$ is the correction-to-update channel. Linearize future margins as
\begin{{equation}}
    m_j(\theta + Jc) \approx a_j^\top \theta + a_j^\top Jc - b_j.
\end{{equation}}
Stacking rows yields
\begin{{equation}}
    Hc \geq h, \quad H = AJ,\quad h = b + \gamma\mathbf{{1}} - A\theta.
\end{{equation}}
UBC solves
\begin{{equation}}
    c^\star = \arg\min_c \|c\|_2^2 \quad \textrm{{s.t.}} \quad Hc \geq h.
    \label{{eq:ubc}}
\end{{equation}}

\begin{{proposition}}[Local certificate]
For the affine update and linear margin model above, Equation~\ref{{eq:ubc}} returns the unique minimum Euclidean-norm physical correction whenever the feasible set is nonempty. If the feasible set is empty, no physical correction in the modeled channel can certify all specified future margins. Any component in $\mathrm{{Null}}(H)$ leaves all certified future margins unchanged.
\end{{proposition}}

\textit{{Proof sketch.}} The feasible set is an intersection of halfspaces and is therefore convex. Projecting the origin onto a nonempty closed convex set has a unique Euclidean projection. Infeasibility means the halfspaces have empty intersection in the correction coordinates. Finally, if $v \in \mathrm{{Null}}(H)$, then $H(c+v)=Hc$, so $v$ can change the physical motion without changing the certified future margins. A fuller proof is in Appendix~\ref{{app:proof}}.

\section{{Experiments}}
We construct a compact embodied-correction environment that isolates the assumption under test. Each trial samples a future-margin/update map $H=AJ$ and required margin vector $h$. Reachable trials are generated from a hidden feasible physical correction. Unreachable trials contain contradictory constraints in the correction channel. Methods receive only $H$ and $h$.

\textbf{{Methods.}} UBC solves Equation~\ref{{eq:ubc}} exactly by active-set enumeration in the three-dimensional correction space. Current-only applies the minimum correction for the first margin only. Single-axis current uses the largest current-margin coordinate, modeling a teacher or interface that corrects one salient physical direction. Gradient line search moves along the aggregate violated-margin gradient. Random search samples feasible corrections under the physical norm cap.

\textbf{{Metrics.}} We report future success on reachable trials, detection of unreachable trials, and physical norm on successful reachable trials. Future success requires all future margins to be satisfied, not only the current interaction.

\begin{{table}}[t]
\centering
\caption{{Runnable simulated evidence. Rates are percentages except norm.}}
\begin{{tabular}}{{lccc}}
\toprule
Method & Future success & Unreachable detected & Mean norm \\
\midrule
{table}
\bottomrule
\end{{tabular}}
\label{{tab:results}}
\end{{table}}

\begin{{figure}}[t]
\centering
\begin{{minipage}}{{0.48\linewidth}}
\centering
\includegraphics[width=\linewidth]{{figures/success_rates.png}}
\end{{minipage}}
\begin{{minipage}}{{0.48\linewidth}}
\centering
\includegraphics[width=\linewidth]{{figures/correction_norms.png}}
\end{{minipage}}
\caption{{Left: future success and unreachable detection. Right: physical correction norm on successful reachable trials.}}
\label{{fig:results}}
\end{{figure}}

The result is the intended stress test. Current-only corrections can satisfy the immediate margin while failing the future-context set. UBC succeeds on reachable local problems because it solves the exact projected halfspace problem; on contradictory problems it reports infeasibility. This is not evidence that UBC is a complete robot teacher. It is evidence that the distinction between current repair and future-behavior change is operational and measurable.

\section{{Limitations}}
The guarantee is local to the affine update and linearized future-margin model. The finite context set $\mathcal{{Z}}$ is chosen by the designer and may miss deployment cases. The correction cost is Euclidean in the simulator rather than biomechanical. The experiments are abstract and do not include hardware contact, tactile sensing, or a high-dimensional policy. These limitations are central to the paper's honest scope: MEC is a formal object and UBC is a local certificate, not a universal account of human teaching.

\section{{Conclusion}}
Physical correction papers often conflate immediate repair with future robot learning. Minimum Effective Correction separates them. By projecting physical effort through the robot's update channel, UBC identifies the smallest correction that can change future behavior under a local model, and it exposes when the interface cannot provide such a correction. The mechanism is small, but the shift is sharp: the central question becomes not only what the human intended, but what the robot learner can actually absorb.

\bibliographystyle{{iclr2026_conference}}
\bibliography{{references}}

\appendix
\section{{Proof Details}}
\label{{app:proof}}
Consider $C=\{{c:Hc\ge h\}}$. If $C$ is nonempty, it is closed and convex. The function $f(c)=\frac12\|c\|_2^2$ is strongly convex, so it has at most one minimizer on $C$. Since $C$ is closed and $f$ is coercive, the minimizer exists. Therefore the solution of Equation~\ref{{eq:ubc}} is the unique minimum-norm correction in the local model.

If $C$ is empty, then by definition there is no correction vector satisfying all local future-margin constraints. This is a statement about the current correction channel $H=AJ$, not about the task in general. A different learner, feature map, or teaching interface can change $H$.

For the nullspace claim, let $v\in\mathrm{{Null}}(H)$. For any candidate correction $c$, the certified margin vector changes from $Hc-h$ to $H(c+v)-h=Hc-h$. Thus effort along $v$ may change contact geometry or compliance, but it cannot change the certified future margins under the modeled learner. This is the formal reason a visually meaningful physical correction can still be learning-irrelevant.

\section{{Reproducibility}}
The experiment can be rerun with:
\begin{{verbatim}}
python scripts/run_experiments.py
\end{{verbatim}}
The literature matrix and synthesis documents can be regenerated with:
\begin{{verbatim}}
python scripts/literature_pipeline.py
python scripts/synthesize_docs.py
\end{{verbatim}}

\end{{document}}
""".strip()
    (PAPER / "main.tex").write_text(tex + "\n", encoding="utf-8")


def main() -> None:
    write_bib()
    write_tex()
    print(f"Wrote paper sources to {PAPER}")


if __name__ == "__main__":
    main()
