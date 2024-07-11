from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from music_py.scales import scale

app = Typer()


@app.command()
def scales(
    tonic=Argument('C', help='Scale tonic'),
    tonality=Argument('major', help='Scale tonality'),
):
    table = Table()
    console = Console()
    notes, degrees = scale(tonic, tonality).values()
    _ = [table.add_column(degree) for degree in degrees]
    table.add_row(*notes)
    console.print(table)
