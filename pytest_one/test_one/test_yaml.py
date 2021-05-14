#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

def test_yaml():
    with open("../data/data.yaml") as f:
        print(yaml.safe_load(f))