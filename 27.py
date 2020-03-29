def deco(fun):
    def inner():
        print("runnning inner()")
        print("11111")
    return inner()

#"""
@deco
def target():
    print("running target()")
#"""
"""
def target():
    print("running target()")
    """
#target = deco(target)
#print(target)
if __name__ == "__main__":
    #pass
    target