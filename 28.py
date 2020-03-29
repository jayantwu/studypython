import register
"""
#register.py#
registry = []
def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')
"""
def main():
    print('running main()')
    print('registry ->', register.registry)
    register.f1()
    register.f2()
    register.f3()
if __name__ == '__main__':
    main()



"""
输出结果
running register(<function f1 at 0x0000019339D133A0>)
running register(<function f2 at 0x0000019339D13040>)
running main()
registry -> [<function f1 at 0x0000019339D133A0>, <function f2 at 0x0000019339D13040>]
running f1()
running f2()
running f3()


"""
