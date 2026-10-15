# Template

<!-- Add a banner here like: https://github.com/StephanAkkerman/fintwit-bot/blob/main/img/logo/fintwit-banner.png -->

---
<!-- Adjust the link of the first and second badges to your own repo -->
<p align="center">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/StephanAkkerman/template/ci.yml?label=python%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13&logo=python&style=flat-square">
  <img src="https://img.shields.io/github/license/StephanAkkerman/template.svg?color=brightgreen" alt="License">
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
</p>

## Introduction

In this section you can provide a brief introduction to the project. You can also include a brief description of the project and its features.

> **Using this template:** click *Use this template* on GitHub. The first push runs the
> `Initialize from template` workflow, which renames `project-name`/`project_name` after
> your repository, fixes the badges and URLs, refreshes `uv.lock`, verifies the result and
> commits it. Delete this note afterwards. To do it by hand:
> `python scripts/init_from_template.py --owner <you> --repo <name>`.

## Table of Contents 🗂

- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Citation](#citation)
- [Contributing](#contributing)
- [License](#license)

## Key Features 🔑

This section is optional. If your project has a lot of features, consider adding a list of key features here.

## Installation ⚙️
<!-- Adjust the link of the second command to your own repo -->

Requires Python 3.10 or newer.

```bash
uv tool install git+https://github.com/StephanAkkerman/template.git
# or: pip install git+https://github.com/StephanAkkerman/template.git
```

For development you need [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
git clone https://github.com/StephanAkkerman/template.git
cd template
make install   # uv sync (creates .venv from uv.lock) + pre-commit hooks
make check     # ruff, ty and pytest: the same gates as CI
```

Dependencies are declared in `pyproject.toml` and pinned in `uv.lock` (there is no `requirements.txt`). Add one with `uv add <package>`.

## Usage ⌨️

```bash
project-name --help
```

See `.env.example` for configuration.

## Citation ✍️
<!-- Be sure to adjust everything here so it matches your name and repo -->
If you use this project in your research, please cite as follows:

```bibtex
@misc{project_name,
  author  = {Stephan Akkerman},
  title   = {Project Name},
  year    = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/StephanAkkerman/template}}
}
```

## Contributing 🛠
<!-- Be sure to adjust the repo name here for both the URL and GitHub link -->
Contributions are welcome! If you have a feature request, bug report, or proposal for code refactoring, please feel free to open an issue on GitHub. We appreciate your help in improving this project.\
![https://github.com/StephanAkkerman/template/graphs/contributors](https://contributors-img.firebaseapp.com/image?repo=StephanAkkerman/template)

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
