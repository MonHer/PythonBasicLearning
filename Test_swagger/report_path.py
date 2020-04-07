# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/07/19:06
# @Author : Yuye
# @File   : report_path.py

import configparser
import os

# 创建实例
# 加载配置文件
# 根据section option获取值


class ReadConfig:

    # 初始化函数：实例化conf对象，读取传入的配置文件
    def __init__(self, contants):
        self.conf = configparser.ConfigParser()
        file = os.path.join(contants.conf_dir,'global.conf')
        self.conf.read(file)
        if self.get_config_boolean('switch','button'):
            test_conf = os.path.join(contants.conf_dir,'test_env.conf')
            self.conf.read(test_conf)
        else:
            online_conf = os.path.join(contants.conf_dir,'online_env.conf')
            self.conf.read(online_conf)

    def get_config_str(self,section,option):
        return self.conf.get(section,option)

    def get_config_boolean(self,section,option):
        return self.conf.getboolean(section,option)

    def get_config_int(self,section,option):
        return self.conf.getint(section,option)

    def get_config_float(self,section,option):
        return self.conf.getfloat(section,option)