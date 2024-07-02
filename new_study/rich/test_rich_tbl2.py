from rich.table import Table
from rich.console import Console
rich_tbl = Table('Name', 'Age', 'hobby')

rich_tbl.title = ' people'

rich_tbl.add_row('Lisa', '33', 'coding')
rich_tbl.add_row('tiny', '22', 'fighting')

rich_tbl.add_section()

rich_tbl.add_row('lily', '44', 'cooking')


console = Console()
console.print(rich_tbl)


'''
          people         
┏━━━━━━┳━━━━━┳━━━━━━━━━━┓
┃ Name ┃ Age ┃ hobby    ┃
┡━━━━━━╇━━━━━╇━━━━━━━━━━┩
│ Lisa │ 33  │ coding   │
│ tiny │ 22  │ fighting │
├──────┼─────┼──────────┤
│ lily │ 44  │ cooking  │
└──────┴─────┴──────────┘
'''