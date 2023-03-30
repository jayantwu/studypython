class Myclass:
    i = 12345

    def f(self):
        return 'hello world'
    def f2(self, x):
        print("hello {}".format(x))

    



x = Myclass()

print(x.f())

x.f2(5)

print(Myclass.f(x))

Myclass.f2(x, 6)

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    e = Dog('buddy')
    d = Dog('fido')









