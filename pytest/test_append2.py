# contents of test_append.py
import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True) # 会自动发生， 自动调用
def append_first(order, first_entry):
    #print("call append_first")
    return order.append(first_entry)


def test_string_only(order, first_entry):
    #print("call test_string_only")
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    #print("call test_string_and_int")
    order.append(2)
    assert order == [first_entry, 2]

def test_string_and_int2(order, first_entry):
    #print("call test_string_and_int2")
    order.append(2)
    assert order == [first_entry, 2]