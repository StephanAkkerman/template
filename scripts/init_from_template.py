"""Turn a fresh copy of this template into a project named after its repository.

Run by ``.github/workflows/init-template.yml`` on the first push to a repository
created from the template. It can also be run by hand::

    python scripts/init_from_template.py --owner octocat --repo my-tool

What it does, using only the standard library:

* ``project-name`` -> the repository name (distribution/CLI name)
* ``project_name`` -> the repository name as a Python identifier (import name)
* ``src/project_name/`` -> ``src/<identifier>/``
* ``StephanAkkerman/template`` -> ``<owner>/<repo>`` (badges, URLs, citation)
* the README title, the copyright/citation year and the funding handle
* removes this script, since it has done its job

The caller is expected to run ``uv lock`` afterwards (the project name is in
``uv.lock``).
"""

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

TEMPLATE_SLUG = "StephanAkkerman/template"
TEMPLATE_OWNER = "StephanAkkerman"
PLACEHOLDER_DIST = "project-name"
PLACEHOLDER_PACKAGE = "project_name"

ROOT = Path(__file__).resolve().parent.parent
# Never rewritten: regenerated (uv.lock) or the files that implement the init.
SKIP = {
    "uv.lock",
    "scripts/init_from_template.py",
    ".github/workflows/init-template.yml",
}


def to_distribution(repo: str) -> str:
    """Normalise a repository name to a PEP 503 style distribution name.

    Parameters
    ----------
    repo : str
        Repository name, e.g. ``My.Cool_tool``.

    Returns
    -------
    str
        Lowercase name with runs of ``-``, ``_`` and ``.`` collapsed to ``-``.
    """
    return re.sub(r"[-_.]+", "-", repo).strip("-").lower()


def to_package(repo: str) -> str:
    """Turn a repository name into a valid Python package name.

    Parameters
    ----------
    repo : str
        Repository name, e.g. ``my-cool-tool``.

    Returns
    -------
    str
        Lowercase identifier, e.g. ``my_cool_tool``; prefixed with ``_`` if it
        would otherwise start with a digit.
    """
    name = re.sub(r"[^0-9a-zA-Z]+", "_", repo).strip("_").lower()
    return f"_{name}" if name[:1].isdigit() else name


def tracked_files() -> list[str]:
    """List the files tracked by git, relative to the repository root.

    Returns
    -------
    list[str]
        Paths using forward slashes.
    """
    out = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [p for p in out.stdout.split("\0") if p]


def rewrite(text: str, owner: str, repo: str, dist: str, package: str) -> str:
    """Apply the placeholder substitutions to one file's contents.

    Parameters
    ----------
    text : str
        Original file contents.
    owner : str
        GitHub user or organisation that owns the new repository.
    repo : str
        Name of the new repository.
    dist : str
        Distribution/CLI name replacing ``project-name``.
    package : str
        Import name replacing ``project_name``.

    Returns
    -------
    str
        The rewritten contents.
    """
    year = str(date.today().year)

    # Case-insensitive so lowercase image names (ghcr.io/...) are covered too;
    # keep the lowercase form where the original was lowercase.
    def slug(match: re.Match[str]) -> str:
        new = f"{owner}/{repo}"
        return new.lower() if match.group(0).islower() else new

    text = re.sub(re.escape(TEMPLATE_SLUG), slug, text, flags=re.IGNORECASE)
    text = text.replace(PLACEHOLDER_DIST, dist).replace(PLACEHOLDER_PACKAGE, package)
    text = re.sub(r"^# Template$", f"# {repo}", text, flags=re.MULTILINE)
    text = re.sub(r"(Copyright \(c\) )\d{4}", rf"\g<1>{year}", text)
    text = re.sub(r"(year\s*=\s*\{)\d{4}(\})", rf"\g<1>{year}\2", text)
    return text.replace(f"github: [{TEMPLATE_OWNER}]", f"github: [{owner}]")


def main(argv: list[str] | None = None) -> int:
    """Run the initialisation.

    Parameters
    ----------
    argv : list[str] | None, optional
        Arguments to parse, defaults to ``sys.argv[1:]``.

    Returns
    -------
    int
        Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--owner", required=True, help="GitHub user or organisation")
    parser.add_argument("--repo", required=True, help="repository name")
    parser.add_argument("--dry-run", action="store_true", help="only print the plan")
    args = parser.parse_args(argv)

    dist, package = to_distribution(args.repo), to_package(args.repo)
    if not package.isidentifier():
        print(
            f"error: {args.repo!r} does not give a valid package name", file=sys.stderr
        )
        return 1
    old_dir, new_dir = ROOT / "src" / PLACEHOLDER_PACKAGE, ROOT / "src" / package
    if not old_dir.is_dir():
        print("Nothing to do: src/project_name/ is already renamed.")
        return 0

    print(f"{args.owner}/{args.repo}: distribution={dist} package={package}")
    changed = []
    for rel in tracked_files():
        path = ROOT / rel
        if rel in SKIP or not path.is_file():
            continue
        try:
            old = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # binary file
        new = rewrite(old, args.owner, args.repo, dist, package)
        if new != old:
            changed.append(rel)
            if not args.dry_run:
                path.write_text(new, encoding="utf-8")
    print("rewrote:", *changed, sep="\n  ")

    if args.dry_run:
        print(
            f"would rename {old_dir.relative_to(ROOT)} -> {new_dir.relative_to(ROOT)}"
        )
        return 0
    if package != PLACEHOLDER_PACKAGE:
        subprocess.run(["git", "mv", str(old_dir), str(new_dir)], cwd=ROOT, check=True)
    Path(__file__).unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
