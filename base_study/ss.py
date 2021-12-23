#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
def test_login():
    data = {
        "account": 13589734158,
        "localPassword": "abc123",
    }
    head= {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    s = requests.post(f"http://10.50.22.159:8887/login",
                      data =data,headers = head)

    print(s.json())





