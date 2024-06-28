import pytest

@pytest.fixture
def make_people():
    peoples = []
    def _make_people(name):
        peoples.append(name)
        return name
    
    print("before")
    
    yield _make_people

    for n in peoples:
        print(n)


def test_make_people(make_people):
    make_people("sally")
    make_people("tony")
    make_people("Joe")

