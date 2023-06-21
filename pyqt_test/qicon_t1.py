# -*- coding: utf-8 -*-
# @File    : qicon_t1.py
# 功能：
# @Time    : 2023/5/25 9:11
# @Author  : lhy
# @Software: PyCharm


from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap, QIcon
from PyQt5.QtCore import Qt


class CustomWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Custom Widget')
        self.setFixedSize(400, 300)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.draw_icon_action = QAction(QIcon('draw_icon.png'), 'Draw Line', self)
        self.draw_icon_action.triggered.connect(self.draw_line)
        self.toolbar.addAction(self.draw_icon_action)

    def draw_line(self):
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置画笔属性
        pen = QPen(Qt.red)
        pen.setWidth(2)
        painter.setPen(pen)

        # 在指定的区域内画直线
        line_rect = pixmap.rect().adjusted(8, 8, -8, -8)
        painter.drawLine(line_rect.topLeft(), line_rect.bottomRight())

        painter.end()

        icon = QIcon(pixmap)
        self.draw_icon_action.setIcon(icon)


if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget()
    widget.show()
    app.exec_()
