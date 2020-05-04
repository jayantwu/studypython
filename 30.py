def deco1(func):
    def f():
        print("i am a boy!!")
    return f

def deco2(func):
    def f():

        print("more information --> i am 19 years old!")

        result = func()
        return result
    return f

@deco1
def f1():
    print("aa")


@deco2
def f2():
    print("i'm a boy!")

f1()
f2()



"""
output:

i am a boy!!
more information --> i am 19 years old!
i'm a boy!

"""
