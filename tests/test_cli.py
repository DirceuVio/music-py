from pytest import mark
from typer.testing import CliRunner

from music_py.cli import app

runner = CliRunner()


def test_scales_cli_stdout_should_return_0():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('note', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
def test_scale_cli_should_contain_notes(note):
    result = runner.invoke(app)
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_F_scale_cli_should_contain_notes(note):
    result = runner.invoke(app, ['F'])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_F_scale_cli_should_contain_degrees(degree):
    result = runner.invoke(app)
    assert degree in result.stdout
