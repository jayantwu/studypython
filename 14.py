# 多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
# 在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）
# 。也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
# 上述代码子类是约定俗称的实现这个方法，加上@abstractmethod装饰器后严格控制子类必须实现这个方法
from abc import ABCMeta, abstractmethod

class Person(object, metaclass=ABCMeta):   #如果定义了metaclass=ABCMeta,则这个类不能被实例化，是一个抽象类！！！！
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)
    @abstractmethod   #实现抽象类的功能
    def wear(self):
        pass


class Student(Person):
    """学生"""
    """不同之处，super（）"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

    def wear(self):
        print("学生穿校服！")


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

    def wear(self):
        print("老师穿西装！")


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_tv()
    stu.wear()
    t = Teacher('tony', 25, '老师')
    t.teach('Python程序设计')
    t.watch_tv()
    t.wear()
    """看到有人说由于定义了abstractmethod抽象方法，这个Person类不能直接实例化？？"""
    """实际测试在定义抽象方法之后，仍然可以创建对象。PS："""
    """
    person = Person("xiaoming", 22)
    person.play()
    print(person)
    """

if __name__ == '__main__':
    main()