import pytest
import yaml


@pytest.fixture(params=["a","b","c"],ids=["name1","name2","name3"])
def login(request):
    return request.param

# def test_a(login):
#     print(login)


print(yaml.safe_load(open("./data/data2.yaml")))