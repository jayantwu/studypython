import json

a = json.dumps([1, 'simple', 'list'])


print(a)

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    name = "wujiayang"



with open('txt1', 'r+') as f:
    json.dump(["hello world", "wujiayang"], f)
    a = A(1, 2)

    json.dump(a.__dict__, f)

