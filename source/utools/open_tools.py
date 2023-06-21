# -*- coding: utf-8 -*-
# @File    : open_tools.py
# 功能：
# @Time    : 2023/5/17 11:11
# @Author  : lhy
# @Software: PyCharm
from osgeo import gdal
import pandas as pd
from osgeo import ogr
from PyQt5.QtWidgets import QApplication, QFileDialog
import shapefile
import geopandas as gpd
import logging
import math

# 墨卡托坐标系范围
x = [-20037508.3427892,20037508.3427892]
y = [-20037508.3427892,20037508.3427892]


def read_shp_file(shp_file):
    """geopandas读取数据"""
    geo_data_ma = {}
    file_name = shp_file.split("/")[-1].split(".")[0]
    geo_data = gpd.read_file(shp_file, encodings="gbk").to_crs("EPSG:3857")
    data_type = geo_data.geom_type[0]
    geo_data_ma["file_name"] = file_name
    geo_data_ma["data_type"] = data_type
    geo_data_ma["attribute"] = geo_data[geo_data.columns[0:-2]]
    geo_data_ma["shape"] = geo_data.geometry
    # print("坐标位置",geo_data.geometry[0].xy)

    return geo_data_ma


class OpenFile:
    """文件读取"""
    def __init__(self):
        self.file_path = None
        self.type = None
        self.file_dict = None

    def open_file(self):
        # 打开文件对话框
        file_name_list, _ = QFileDialog.getOpenFileNames(None, "打开文件", "", "道路网络文件 (*.shp)")
        print(file_name_list)
        if file_name_list is None:
            logging.info("file_name_list is empty")
            print("file is empty")
            return
        for file_name in file_name_list:
            # print(file_name)
            self.file_dict = read_shp_file(file_name)


    def get_by_gdal(self,shp_file):
        """shp读取"""
        pass

    def get_shp_file(self):
        pass


def lonLat2WebMercator(lon, lat):
    x = lon * 20037508.34 / 180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * 20037508.34 / 180
    return [x, y]

def webMercator2LonLat(x, y):
    lon = x / 20037508.34 * 180
    lat = y / 20037508.34 * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    return [lon, lat]