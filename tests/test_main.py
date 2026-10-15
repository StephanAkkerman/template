import logging
import runpy

import pytest

from project_name import __version__
from project_name.main import main


def test_main_runs(caplog):
    caplog.set_level(logging.INFO)
    assert main([]) == 0
    assert "Hello World" in caplog.text


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert __version__ in capsys.readouterr().out


def test_module_entry_point(monkeypatch):
    monkeypatch.setattr("sys.argv", ["project-name"])
    with pytest.raises(SystemExit) as exc:
        runpy.run_module("project_name", run_name="__main__")
    assert exc.value.code == 0
