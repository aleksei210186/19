import pytest

from App.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 10, 2) == 20

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_adding_success(self):
        assert self.calc.adding(self, 10, 2) == 12

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_divisiom(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода teardown')