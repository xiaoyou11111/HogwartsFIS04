# - 补全计算器（加法，除法）的测试用例
# - 使用数据驱动完成测试用例的自动生成
# - 在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

import pytest
import yaml

from pycode.caculator.caculator import caculator


class TestCal:
    # 获取yaml文件所有数据
    data = yaml.safe_load(open("./data.yaml"))

    def setup_class(self):
        self.cal = caculator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    # @pytest.mark.parametrize(("a", "b", "expect"), [[1, 2, 3], [1, 1, 2]])
    @pytest.mark.parametrize(("a", "b", "expect"), data["add_int"])
    def test_add_int(self, a, b, expect):
        assert self.cal.add(a, b) == expect

    # @pytest.mark.parametrize('a, b, expect', [[0.1, 0.2, 0.3], [0.1, 0.1, 0.2]])
    @pytest.mark.parametrize('a, b, expect', data["add_float"])
    def test_add_float(self, a, b, expect):
        assert round(self.cal.add(a, b), 1) == expect

    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.cal.div(1, 0)

    # @pytest.mark.parametrize(['a', 'b', 'expect'], [[1, 2, 0.5], [6, 3, 2], [0.5, 0.2, 2.5]])
    @pytest.mark.parametrize(['a', 'b', 'expect'], data["div"])
    def test_div(self, a, b, expect):
        assert self.cal.div(a, b) == expect
