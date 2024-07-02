import rich_common as rich_cmn
from rich.table import Table
import json

def gen_tbl(path):
    with open(path, 'r') as f:
        data = json.load(f)
    table = Table(title="Python Rich Table")
    table.add_column("Name", style="cyan", justify="right")
    table.add_column("Age", style="magenta", justify="right")
    table.add_column("hobby", style="green", justify="right")
    for item in data:
        table.add_row(item["name"].title(), str(item["age"]), item["hobby"])
    rich_cmn.show(table)

if __name__ == "__main__":
    gen_tbl('./people.json')
