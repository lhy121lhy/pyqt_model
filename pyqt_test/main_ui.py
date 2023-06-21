# -*- coding: utf-8 -*-
# @File    : main_ui.py
# 功能：
# @Time    : 2023/5/20 19:07
# @Author  : lhy
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口的标题和大小
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        # 创建一个QWidget对象，并将其设置为主窗口的中央部件
        # widget = QWidget(self)
        # self.setCentralWidget(widget)
        self.custom_widget = CustomWidget()

        # 将自定义小部件设置为主窗口的中央部件
        self.setCentralWidget(self.custom_widget)

        # 创建一个标签，并将其添加到QWidget中
        # label = QLabel("Hello, World!", widget)
        # label.setGeometry(50, 50, 200, 50)

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建一个标签，并将其添加到自定义小部件中
        label = QLabel("Custom Widget", self)
        label.setGeometry(50, 50, 200, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # custom_widget = CustomWidget()
    # custom_widget.show()

    sys.exit(app.exec_())

