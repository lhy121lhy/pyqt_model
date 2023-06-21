# -*- coding: utf-8 -*-
# @File    : qtable_view_widget.py
# 功能：
# @Time    : 2023/6/13 21:45
# @Author  : lhy
# @Software: PyCharm

import csv
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget
import sys


class TableView(QTableWidget):
    # 创建显示窗口
    def __init__(self, data):
        super().__init__()
        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))
        self.setHorizontalHeaderLabels(data[0])

        for i in range(1, len(data)):
            for j in range(len(data[0])):
                self.setItem(i, j, QTableWidgetItem(data[i][j]))

        self.resizeColumnsToContents()



