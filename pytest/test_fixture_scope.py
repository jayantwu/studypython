import pytest

@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup for module")
    data = {"key": "value"}
    yield data
    print("\nTeardown for module")

def test_example1(setup_module):
    assert setup_module["key"] == "value"

def test_example2(setup_module):
    assert len(setup_module) == 1