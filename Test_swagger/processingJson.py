# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/07/17:10
# @Author : Yuye
# @File   : processingJson.py

import json
from Test_swagger.logger import Log



def write_data(res, json_path):
    """把处理后的参数写入json文件"""
    if isinstance(res, dict):
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=4)
            Log().info('Interface Params Total：{} ,write to json file successfully!\n'.format(len(res)))
    else:
        Log().info('{} Params is not dict.\n'.format(write_data.__name__))