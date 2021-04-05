import allure
import pytest


@allure.feature("计算功能")
class TestCal1:
    @allure.story("整数相加功能")
    def test_add_int(self, get_data1, func):
        assert func.add(get_data1[0], get_data1[1]) == get_data1[2]

    @allure.story("浮点数相加功能")
    def test_add_float(self, get_data2, func):
        assert round(func.add(get_data2[0], get_data2[1]), 1) == get_data2[2]

    @allure.story("相处功能")
    def test_div(self, get_data3, func):
        assert func.div(get_data3[0], get_data3[1]) == get_data3[2]

    @allure.story("除零功能")
    def test_div_zero(self, get_data4, func):
        with pytest.raises(ZeroDivisionError):
            func.div(get_data4[0], get_data4[1])
