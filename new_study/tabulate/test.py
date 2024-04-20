from tabulate import tabulate

table = [['name', 'age', 'score'], ['sally', 23, 98], ['tony', 22, 78], ['jacky', 25, 77]]

tabulate_tbl = tabulate(table, headers='firstrow')


tabulate_tbl2 = tabulate(table, headers='firstrow', tablefmt='github')


tabulate_tbl3 = tabulate(table, headers='firstrow', tablefmt='grid')
print(tabulate_tbl)

print()

print(tabulate_tbl2)

print()

print(tabulate_tbl3)