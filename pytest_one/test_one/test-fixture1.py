#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def login():
    print("登录")
    yield 


class TestDemo1():
    
    def setup(self):
        # 第一步，打开浏览器；
        pass

    def setup_class(self):
        # 第一步，打开浏览器；--类的开始
        pass

    def teardown_class(self):
        # 第五步，关闭浏览器--类的结束
        pass
    def teardown(self):
        # 第五步，关闭浏览器
        pass
    
        
    def test_a(self):
        # 第二步，输入网址；第三步，定位；第四步，各种操作；
        pass
    
    def tset_b(self):
        pass
    
    def