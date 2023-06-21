# -*- coding: utf-8 -*-
# @File    : opengl_test1.py
# 功能：
# @Time    : 2023/5/18 15:29
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtGui import QImage, QPainter, QMouseEvent, QColor
from PyQt5.QtCore import Qt

class ImageWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage()  # 用于存储图像
        self.offset = (0, 0)  # 图像的偏移量
        self.last_pos = None  # 上次鼠标位置
        self.scale_factor = 1.0

    def loadImage(self, filename):
        self.image.load(filename)
        self.update()

    def wheelEvent(self, event):
        delta = event.angleDelta().y() / 120
        if delta > 0:
            self.scale_factor *= 1.1
        else:
            self.scale_factor *= 0.9
        self.update()

        # numDegrees = event.angleDelta().y() / 8
        # numSteps = numDegrees / 15
        # self.scale += numSteps * 0.01
        # self.update()

    def resizeEvent(self, event):
        # 当窗口大小改变时，需要更新图片的尺寸
        self.update()

    def sizeHint(self):
        # 设置窗口的初始大小
        return self.image.size() * self.scale_factor

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        print("鼠标平移:")
        if event.buttons() == Qt.LeftButton and self.last_pos:
            # 计算鼠标的偏移量
            dx = event.pos().x() - self.last_pos.x()
            dy = event.pos().y() - self.last_pos.y()

            # 更新图像的偏移量
            self.offset = (self.offset[0] + dx, self.offset[1] + dy)
            self.update()

            # 更新鼠标位置
            self.last_pos = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.last_pos = None

    def paintGL(self):
        painter = QPainter(self)
        painter.beginNativePainting()

        # 清除画布
        painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        # 绘制图像
        # painter.drawImage(0, 0, self.image.scaled(self.image.width() * self.scale_factor,
        #                                           self.image.height() * self.scale_factor,
        #                                           Qt.KeepAspectRatio))
        # painter.drawImage(self.offset[0], self.offset[1], self.image)
        painter.drawImage(self.offset[0], self.offset[1], self.image.scaled(int(self.image.width() * self.scale_factor),
                                                  int(self.image.height() * self.scale_factor),
                                                  Qt.KeepAspectRatio))

        painter.endNativePainting()
        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    viewer = ImageWidget()
    viewer.loadImage('input/image.PNG')  # 替换为您的图像路径
    window.setCentralWidget(viewer)
    window.show()
    app.exec_()
