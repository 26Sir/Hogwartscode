#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SoftAssertion:
    def __init__(self):
        self.succes = True
        self.err_message = []
        
    def check(self,to_cehck,err_message):
        self.succes = self.succes and to_cehck
        if not to_cehck:
            self.err_message.append(err_message)


if __name__ == '__main__':
    soft_asser = SoftAssertion()
    a =1
    b =2
    c=3
    d=2
    soft_asser.check((a+b==c),f"a+b应该等于c")
    soft_asser.check((a+c==d),f"a+b应该等于d")
    soft_asser.check((a+d==c),f"a+b应该等于d")
    soft_asser.check((a is None),f"a是None")
    soft_asser.check((a is b),f"a和b一样")
    assert soft_asser.succes,soft_asser.err_message