import pytest


@pytest.fixture(scope="module", params=['hello', 'world'])
def set_up(request):
    print(request.param)
    yield request.param
    print('test end')
    



def test_param(set_up):
    print(f'testing....{set_up}')

def test_param2(set_up):
    print(f'testing2....{set_up}')


"""
out put:
test_param.py hello
testing....hello
.testing2....hello
.test end
world
testing....world
.testing2....world
.test end

用第一个参数执行 test1, test2, 在用第二个参数执行test1 test2
"""
