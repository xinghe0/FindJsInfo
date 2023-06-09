# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/6 7:19 PM
@Auth ： xinghe
@File ：findjs_api.py
@IDE ：PyCharm
@Motto:但行好事，莫问前程
"""

import os

def findjs_cmd(path):
    os.system(f"python common/FindJsInfo/run.py -l {path}")

findjs_cmd('../../results/all_subdomain_result_20230609_141151_web.txt')