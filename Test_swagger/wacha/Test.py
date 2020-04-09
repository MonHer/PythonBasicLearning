# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/09/15:29
# @Author : Yuye
# @File   : Test.py


from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.chrome()
driver.get(url)
