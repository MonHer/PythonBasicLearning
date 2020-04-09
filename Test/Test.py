# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/09/17:23
# @Author : Yuye
# @File   : Test.py


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('http://test-web.xinkangzaixian.cn')

# driver.implicitly_wait(10)
loc = (By.XPATH, '//*[@type="text" and @placeholder="请输入账号"]')
try:
    WebDriverWait(driver,20,0.5).until(EC.presence_of_all_elements_located(loc))
    print("进入登录页面")
except:
    print("进入失败")
driver.find_element_by_xpath('//*[@type="text" and @placeholder="请输入账号"]').send_keys("qq")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@type="password" and @placeholder="请输入密码"]').send_keys("123456")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@type="text" and @placeholder="请输入验证码"]').send_keys("5555")
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@type="button"]').click()
print("登录成功")
driver.quit()