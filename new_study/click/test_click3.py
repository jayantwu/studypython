import click

@click.group()
def main():
    pass


@click.group()
def set():
    pass


@set.command
@click.option("--name", type=str,  help="input your name")
def show(name):
    click.echo(f"your name is {name}")

@set.command
@click.option("-n", "--num",  type=str,  help="input a num")
def show2(num):
    click.echo(f"num = {num}")

@click.group()
def get():
    pass

@get.command
@click.option("--id", type=int,  help="input your id")
def show_id(id):
    click.echo(f"id is {id}")

main.add_command(set)
main.add_command(get)

if __name__ == "__main__":
    main()