# -*- coding: utf-8 -*-
# @File    : toolbox_treewidget.py
# 功能：
# @Time    : 2023/5/17 9:14
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QTreeWidget

class toolbox_tree_widget(QTreeWidget):
    def __init__(self):
        super().__init__()

        self.setHeaderLabel("toolbox")




