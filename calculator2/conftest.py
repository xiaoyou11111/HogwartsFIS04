import pytest
import yaml

from pycode.calculator2.calculator import calculator


@pytest.fixture(scope="class")
def func():
    print("计算开始")
    cal = calculator()
    yield cal
    print("计算结束")


def getDatas():
    datas = yaml.safe_load(open("./data/data.yaml"))
    return datas


# def getDatas2():
#     datas = yaml.safe_load(open("./data/data2.yaml"))
#     return datas

@pytest.fixture(params=getDatas()['add_int']['data'], ids=getDatas()["add_int"]['ids'])
def get_data1(request):
    return request.param


@pytest.fixture(params=getDatas()['add_float']['data'], ids=getDatas()["add_float"]['ids'])
def get_data2(request):
    return request.param


@pytest.fixture(params=getDatas()['div']['data'], ids=getDatas()["div"]['ids'])
def get_data3(request):
    return request.param


@pytest.fixture(params=getDatas()['div_zero']['data'], ids=getDatas()["div_zero"]['ids'])
def get_data4(request):
    return request.param

# @pytest.fixture(params=getDatas()['data'],ids=getDatas()['ids'])
# def get_data2(request):
#     return request.param
#
# def test1(get_data2):
#     print(get_data2)
