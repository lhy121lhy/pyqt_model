# -*- coding: utf-8 -*-
# @File    : qtabwidget.py
# 功能：
# @Time    : 2023/6/11 12:35
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QApplication,QVBoxLayout
import sys

class TabWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.tab_widget = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        self.tab_widget.addTab(tab1, "Tab 1")
        self.tab_widget.addTab(tab2, "Tab 2")
        self.tab_widget.addTab(tab3, "Tab 3")

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        # self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabWidgetDemo()
    window.show()
    sys.exit(app.exec_())