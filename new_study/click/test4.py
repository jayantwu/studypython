from test_click3 import *
import sys



def main(cmd_args):
    print("Hello World")
    sys.argv = ['test_click3.py'] + cmd_args
    cli()


if __name__ == "__main__":
    main(['my_set', 'show', '--name', 'ffdf'])
