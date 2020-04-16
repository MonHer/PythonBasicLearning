# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/16/16:03
# @Author : Yuye
# @File   : conftest.py

import pytest


@pytest.fixture()
def login():
    print('登陆了')
