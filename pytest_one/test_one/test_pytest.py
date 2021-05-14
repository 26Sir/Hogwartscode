#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from pyone.pytest_one.calc_one.calc import Calc

def steps():
    with open('../data/steps.yaml') as f:
        return yaml.safe_load(f)
        
class TestCalc:
    def setup(self):
        self.calc = Calc()
    
    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (-1, 1, 0), (-1, -3, -4), (0.5, 0.5, 1)])
    def test_add_1(self, a, b, c):
        result = self.calc.add(a, b)
        print(result)
        assert c == result

    
    @pytest.mark.parametrize("a1, b1, expect",
                             yaml.safe_load(open("../data/data.yaml")))
    def test_add2(self, a1, b1, expect):
        
        steps1 = steps()
        for step in steps1:
            print(f"step ===> {step}")
            if 'add' == step:
                result = self.calc.add(a1, b1)
            elif 'add1' == step:
                result = self.calc.add1(a1, b1)
            assert expect == result
            
        # result = self.calc.add(a, b)
        # print(result)
        # assert expect == result
        #
        # result = self.calc.add(a, b)
        # print(result1)
        # assert expect == result1

    
    def test_div(self):
        # self.calc = Calc()
        result_1 = self.calc.div(2, 2)
        print(result_1)
        assert 1 == result_1


if __name__ == '__main__':
    pytest.main()
    # pytest.main(['-vs', 'test_pytest.py::TestCalc::test_add_2'])
