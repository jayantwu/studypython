# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    print("call fisrt_entry")
    return "a"


# Arrange
@pytest.fixture
def order():
    print("call order")
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    print("call append_first")
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]

''' out put: 
test_append.py call order
call fisrt_entry
call append_first
'''


