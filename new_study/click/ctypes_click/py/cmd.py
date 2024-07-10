import click
from ctypes import *
import api
from para import *


@click.group()
def cli():
    pass


@click.group(invoke_without_command=True, name='test1')
@click.pass_context
def test1(ctx):
    pass

# @test1.command
# @click.option("--name", type=str,  help="input your name")
# @click.pass_context
# def create(ctx, name):
#     click.echo(f"para1 is {name}")

@test1.command
@click.option("--para1", type=click_param_TEST1_T(),  help="") # this test1_t is a ctypes struct
@click.option("--para2", type=click_param_TEST2_T(),  help="") # this test2_t is a ctypes struct list
@click.pass_context
def create(ctx, para1, para2):
    click.echo(f"para1 is {para1}")
    print(f"para1 a: {para1.a}, b:{para1.b}")
    p1 = test1_t(para1.a, para1.b) # convert
    print(para2)
    for i in range(para2.cnt):
        print(para2.list[i])
    print(type(para2.list))

    p2 = test2_t(para2.cnt, para2.list)
    #api.create(1, p1, p2) # its ok
    api.create(1, para1, para2)


cli.add_command(create)


if __name__ == "__main__":
    cli()