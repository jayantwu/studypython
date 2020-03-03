class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('{}正在学习{}.'.format(self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('{}只能观看《熊出没》.'.format(self.name))
        else:
            print('{}正在观看岛国爱情大电影.'.format(self.name))

def main():
    stu1 = Student("小明", 25)
    stu1.study("python")
    stu1.watch_movie()


if __name__ == "__main__":
    main()