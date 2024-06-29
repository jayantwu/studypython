# content of test_fixture_marks.py
import pytest


@pytest.fixture(params=['a', 'b', pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass


    """
    xxxx@MacBook-Air pytest % pytest test_fixtrure_mark.py -v
============================================= test session starts ==============================================
platform darwin -- Python 3.9.6, pytest-8.2.2, pluggy-1.5.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/xxxx/xxxx/STUDY/docker/study/xxxx/studypython/pytest
plugins: anyio-4.2.0
collected 3 items                                                                                              

test_fixtrure_mark.py::test_data[0] PASSED                                                               [ 33%]
test_fixtrure_mark.py::test_data[1] PASSED                                                               [ 66%]
test_fixtrure_mark.py::test_data[2] SKIPPED (unconditional skip)                                         [100%]

========================================= 2 passed, 1 skipped in 0.01s =========================================
    """