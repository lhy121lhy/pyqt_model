# -*- coding: utf-8 -*-
# @File    : parameter_set.py
# 功能：系统参数设置
# @Time    : 2023/6/11 11:09
# @Author  : lhy
# @Software: PyCharm
import pandas as pd

import uuid


class ProjectSeting:

    def __init__(self):
        self.data_style = {"layer_index": [],
                           "data_style": {}}

    def append_data(self, data_st):
        u_id = uuid.uuid1()
        self.data_style["layer_index"].append(u_id)
        self.data_style["data_style"][u_id] = {
            "data_type": data_st["data_type"],
            "layer_name": data_st["file_name"],
            "data_attribute": data_st["attribute"],
            "shape": data_st["shape"],
            "default": ""
        }

    def create_set(self,select_sql):
        """选择集创建"""
        pass

    def reset_index(self):
        pass

