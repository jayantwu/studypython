from math import  sqrt

class Point(object):
    """初始化，默认在原点"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    """移动至一个新的点"""
    def move_to(self, x, y):
        self.x = x
        self.y = y
    """移动"""
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
    """other是另一个实例"""
    def distance_to(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


def main():
    p1 = Point(2, 3)
    p2 = Point(-1, 4)
    print("the distance of p1 and p2 is {:.4f}".format(p1.distance_to(p2)))
    p1.move_to(4, 5)
    print(p1)
    print("the distance of p1 and p2 is {:.4f}".format(p1.distance_to(p2)))
    p1.move_by(-2, -1)
    print(p1)
    print("the distance of p1 and p2 is {:.4f}".format(p1.distance_to(p2)))


if __name__ == "__main__":
    main()