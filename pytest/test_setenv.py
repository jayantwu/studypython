import os
import pytest
from study.wujiayang.studypython.pytest.conftest import *


@pytest.mark.usefixtures("cleandir") #放在这里， 而不用放在 测试函数中， 作为一个参数
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        print(os.getcwd())
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []