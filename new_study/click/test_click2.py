import click

@click.group()
def main():
    pass

@main.command
@click.option("--name", type=str,  help="input your name")
@click.option("-n", "--num",  type=str,  help="input a num")
def show(num, name):
    click.echo(f"your name is {name}")
    click.echo(f"num = {num}")

if __name__ == "__main__":
    main()