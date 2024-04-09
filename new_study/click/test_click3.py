import click

@click.group()
def cli():
    pass


@click.group(invoke_without_command=True, name='my_set')
@click.pass_context
def set(ctx):
    pass


@set.command
@click.option("--name", type=str,  help="input your name")
@click.pass_context
def show(ctx, name):
    click.echo(f"your name is {name}")

@set.command
@click.option("-n", "--num",  type=str,  help="input a num")
@click.pass_context
def show2(ctx, num):
    click.echo(f"num = {num}")

@click.group(invoke_without_command=True, name='my_get')
@click.pass_context
def get(ctx):
    pass

@get.command
@click.option("--id", type=int,  help="input your id")
@click.pass_context
def show_id(ctx, id):
    click.echo(f"id is {id}")

cli.add_command(set)
cli.add_command(get)

if __name__ == "__main__":
    cli()