# -*- coding: utf-8 -*-
# @File    : tab_widget_t1.py
# 功能：
# @Time    : 2023/5/25 11:39
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QVBoxLayout,QWidget
from PyQt5.QtGui import QPixmap


class CustomWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Custom Widget')
        self.setFixedSize(600, 400)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.load_images()

    def load_images(self):
        image_files = ['input/image.PNG', 'input/image.PNG', 'input/image.PNG']  # 替换为实际的图片文件路径

        for file in image_files:
            pixmap = QPixmap(file)
            label = QLabel()
            label.setPixmap(pixmap)

            layout = QVBoxLayout()
            layout.addWidget(label)

            widget = QWidget()
            widget.setLayout(layout)

            self.tab_widget.addTab(widget, file)


if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget()
    widget.show()
    app.exec_()
