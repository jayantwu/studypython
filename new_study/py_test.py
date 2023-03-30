import pytest

class Test_py():
    def test_tst01(self):
        print("test1")
        assert True
    def test_tst02(self):
        print("test2")
        assert False
    def test_tst03(self):
        print("test3")
        assert True


if __name__ == "__main__":
    pytest.main(['-v', 'py_test.py::Test_py'])

