# -*- coding: utf-8 -*-
# @File    : write_log.py
# 功能：
# @Time    : 2023/5/19 17:42
# @Author  : lhy
# @Software: PyCharm
import logging

logging.basicConfig(filename='./log.txt', level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')

logging.debug('This is debug message')