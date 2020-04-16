# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/16/10:57
# @Author : Yuye
# @File   : unittest_report.py

import os
import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

import requests

from Test_frame.Unittest_frame.unttest_cs import *


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试类之前的方法")

    def setUp(self) -> None:
        print("这是每一个测试方法前面运行的方法")

    def test_first(self):
        print("这是测试方法1-进行接口测试demo")
        # 这是利用requests第三方库（进行发请求，收响应）向百度发个get请求
        url = "http://www.baidu.com'"
        res = requests.get(url)
        # 这是输出返回结果
        print(res.text)

    def test_second(self):
        print("这是测试方法2-研究一下python的断言")
        assert 1 == 1
        assert {'name': '倪霸霸', 'age': 188} == {'name': '倪霸霸', 'age': 188}
        a = 'hello'
        age = 35
        assert a in 'hello world'
        assert 20 < age < 80
        print("这是测试方法2-研究一下unittest的断言")
        self.assertGreater(1, 1, '这是不可能的')
        self.assertIn(a, ' world', msg='没有hello呀')

    def test_third(self):
        print("这是测试方法3-单元测试-测试开发写的计算器的代码功能是否能实现")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))
        self.assertEqual(1, minus(3, 2))
        self.assertEqual(6, multi(3, 2))
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2, divide(4, 2))

    @classmethod
    def tearDownClass(cls):
        print("这是测试整个类后要执行的方法")


if __name__ == '__main__':
    # sys.path.append('r"D:\GHost\PythonBasicLearning\Test_frame\Unittest_frame')
    # 设置报告的路径
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    # 通过当前时间命名报告
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = report_path + "/" + now + "_result.html"
    # 建立一个套件-就是可以装多个用例
    suite = unittest.TestSuite()
    # 在这个套件中添加测试用例（可能通过类名,模块名等加载，这次用类名）
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClass))
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试用例')
        runner.run(suite)
