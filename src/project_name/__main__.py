"""Allow `python -m project_name`."""

from project_name.main import main

if __name__ == "__main__":
    raise SystemExit(main())
