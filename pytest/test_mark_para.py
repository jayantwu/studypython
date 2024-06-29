import pytest

def addition(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, -1, 3)])
def test_addition0(a, b, expected):
    assert addition(a, b) == expected


test_data = [
    ((1, 2), 3),
    ((2, -1), 1),
    ((4, 2), 6)
]

def pytest_generate_tests(metafunc):
    if 'test_input' in metafunc.fixturenames:
        metafunc.parametrize('test_input, expected_output', test_data)



def test_addition1(test_input, expected_output):
    result = addition(*test_input)
    assert result == expected_output, 'addition failed.'
