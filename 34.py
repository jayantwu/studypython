# test class method
from abc import ABC, abstractmethod
from calendar import c
from this import d
class Animal():
    def __init__(self, name, age, type):
        self._name = name
        self._age = age
        self._type = type
    
    @classmethod
    def dog(cls, name, age):
        return cls(name, age, "dog")

    @classmethod
    def cat(cls, name, age):
        return cls(name, age, "cat")

    def show(self):
        print(f" my name is {self._name}, i'm {self._age} years old, and I'm a {self._type}")

class Pet(ABC):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print("wang wang wang")

class Cat(Pet):
    def make_voice(self):
        print("miao miao miao")



def commentest(fun):
    def decrotor(self):
        print(f"#"*25+ fun.__name__ + " start "+'#'*25)
        fun(self)
        print(f"#"*25+ fun.__name__ + " end "+'#'*25)
        print()
    return decrotor

class Test():

    def run_test(self):
        self.test1()
        self.test2()

    @commentest
    def test1(self):
        #print("#"*25+"test1 start"+'#'*25)
        dog_obj = Animal.dog("carry", 4)
        cat_obj = Animal.cat("tony", 3)

        dog_obj.show()
        cat_obj.show()
        Animal.cat("sarra", 3).show()
        #print("#"*25+"test1 end"+'#'*25)
    @commentest
    def test2(self):
        d = Dog("henry")
        c = Cat("lily")
        d.make_voice()
        c.make_voice()



if __name__ == "__main__":
    Test().run_test()