# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check") # x str no 'check' attr

    def test_three(self):
        x = "world"
        assert hasattr(x, 'upper') # str x has attr 'upper()'
