# content of test_sample.py
def func(x):
    return x + 1


def test_answer0():
    assert func(3) == 4

def test_answer1():
    assert func(3) == 5
