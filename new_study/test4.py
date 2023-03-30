def decorator(func):
    def inner():
        print("start time...")
        func()
        print("end time...")
    return inner

def mylog(func):
    def inner():
        print("log start..")
        func()
        print("leave log...")
    return inner

@mylog
@decorator
def f1():
    print("do task...")


f1()

print("#"*40)

def using_log(level):
    def decorator(func):
        def inner(*args, **kwargs):
            if (level == "warn"):
                print("warn log")
            else:
                print("other level log")
            func(*args)
        return inner
    return decorator


@using_log("warn")
def f2(x):
    print("test f2")
    print(x)

@using_log("other")
def f3(x):
    print("test f3")
    print(x)

f2(2)

f3(3)