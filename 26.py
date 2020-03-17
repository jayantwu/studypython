def fun1():

    x='hello 0.5'
    print('fun1', x, id(x))
    def fun2():
        #global x
        x = 'hello 1'
        print('fun2', x, id(x))
    fun2()
    print('fun1', x, id(x))

x = 'hello 0'
fun1()
print(x, id(x))
"""
def fun1():

    x='hello 0.5'
    print('fun1', x, id(x))
    def fun2():
        nonlocal x
        x = 'hello 1'
        print('fun2', x, id(x))
    fun2()
    print('fun1', x, id(x))

x = 'hello 0'
fun1()
print(x, id(x))

##############################
fun1 hello 0.5 2231496861936
fun2 hello 1 2231526834288
fun1 hello 1 2231526834288
hello 0 2788836925744
nonlocal修饰嵌套函数的变量，该变量不再是内嵌函数的局部变量，变成外部函数的局部变量
###############################
"""

"""
def fun1():

    x='hello 0.5'
    print('fun1', x, id(x))
    def fun2():
        global x
        x = 'hello 1'
        print('fun2', x, id(x))
    fun2()
    print('fun1', x, id(x))

x = 'hello 0'
fun1()
print(x, id(x))

##############################
fun1 hello 0.5 2687334821616
fun2 hello 1 2687334965296
fun1 hello 0.5 2687334821616
hello 1 2687334965296
global修饰嵌套函数的变量时，该变量变成全局变量，与外部函数的局部变量仍然不是同一个
##############################
"""
#如果不加global 或 nonlocal修饰，那么内嵌函数的局部变量，外部函数的局部变量，函数外的全局变量是三个不同的变量