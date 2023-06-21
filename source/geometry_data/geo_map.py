# -*- coding: utf-8 -*-
# @File    : geo_map.py
# 功能：
# @Time    : 2023/5/17 21:11
# @Author  : lhy
# @Software: PyCharm
import pandas as pd


class GeoMap:
    def __init__(self):
        self.geo_list = []
        self.layer_manage = []

    def up_date(self, geo_data):
        leng = len(self.layer_manage)
        file_name = geo_data["file_name"]
        data_type = geo_data["data_type"]
        data_attri = geo_data["attribute"]
        coordata = geo_data["shape"]
        # 状态表：索引，文件名，显示状态，颜色
        self.layer_manage.append([leng+1, file_name, data_type, data_attri, coordata])





