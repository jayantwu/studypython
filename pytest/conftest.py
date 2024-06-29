import os
import tempfile

import pytest
# 这个文件命名成conftest.py 是必须的！！！

@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        print(old_cwd)
        os.chdir(newpath)
        print(newpath)
        yield
        os.chdir(old_cwd)
        print('change back')


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))