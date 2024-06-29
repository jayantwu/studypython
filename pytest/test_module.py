import pytest


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg", param)
    yield param
    print("  TEARDOWN otherarg", param)


def test_0(otherarg):
    print("  RUN test0 with otherarg", otherarg)


def test_1(modarg):
    print("  RUN test1 with modarg", modarg)


def test_2(otherarg, modarg):
    print("  RUN test2 with otherarg {} and modarg {}".format(otherarg, modarg))


"""
test_module.py::test_0[1] PASSED                                                                         [ 12%]
test_module.py::test_0[2] PASSED                                                                         [ 25%]
test_module.py::test_1[mod1] PASSED                                                                      [ 37%]
test_module.py::test_2[mod1-1] PASSED                                                                    [ 50%]
test_module.py::test_2[mod1-2] PASSED                                                                    [ 62%]
test_module.py::test_1[mod2] PASSED                                                                      [ 75%]
test_module.py::test_2[mod2-1] PASSED                                                                    [ 87%]
test_module.py::test_2[mod2-2] PASSED                                                                    [100%]
注意这个执行顺序， 由于 modarg fixture 是模块 scope, 为了让它只加载一次， mod 1 加载之后， 相关的test 都执行了一次
"""



"""
test_module.py::test_0[1] PASSED                                                                         [ 12%]
test_module.py::test_2[1-mod1] PASSED                                                                    [ 25%]
test_module.py::test_1[mod1] PASSED                                                                      [ 37%]
test_module.py::test_2[2-mod1] PASSED                                                                    [ 50%]
test_module.py::test_0[2] PASSED                                                                         [ 62%]
test_module.py::test_2[2-mod2] PASSED                                                                    [ 75%]
test_module.py::test_2[1-mod2] PASSED                                                                    [ 87%]
test_module.py::test_1[mod2] PASSED                                                                      [100%]
如果把otherarg 也改成module scope , 执行顺序变成了这样
"""