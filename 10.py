class Person(object):
    def __init__(self, age=10):
        self._age = age
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def birth(self):
        return 2020-self._age

    def information(self):
        print(self._name, self._age)

class Person2(object):
    def __init__(self, name):
        self.name = name
    """
    @property
    def name(self):
        return self.name

    """
    def print_info(self):
        print(self.name)




if __name__ == "__main__":
    person = Person(22)
    person.name = "小明"
    person.information()
    print(person.birth)
    print(person.name)
    print("*"*40)
    person2 = Person2("小刚")
    print(person2.name)

"""
关于装饰器：
定义装饰器之后，类的属性命名貌似只能使用前导下划线，不使用会报错
property 将类方法用类属性的形式进行调用

"""
