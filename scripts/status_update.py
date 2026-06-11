import argparse
from pathlib import Path


def bullet(lines):
    if not lines:
        return "- None."
    return "\n".join(f"- {line}" for line in lines)


def main():
    parser = argparse.ArgumentParser(description="Rewrite compact child status from current facts.")
    parser.add_argument("--stage", required=True)
    parser.add_argument("--completed", action="append", default=[])
    parser.add_argument("--commands", action="append", default=[])
    parser.add_argument("--failures", action="append", default=[])
    parser.add_argument("--recoveries", action="append", default=[])
    parser.add_argument("--next", action="append", default=[])
    args = parser.parse_args()

    text = (
        "# Child Status\n\n"
        f"Stage: {args.stage}\n\n"
        "Completed:\n"
        f"{bullet(args.completed)}\n\n"
        "Current or recent commands:\n"
        f"{bullet(args.commands)}\n\n"
        "Failures:\n"
        f"{bullet(args.failures)}\n\n"
        "Recovery steps:\n"
        f"{bullet(args.recoveries)}\n\n"
        "Next:\n"
        f"{bullet(getattr(args, 'next'))}\n"
    )
    Path("child_status.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
