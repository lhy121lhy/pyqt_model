# -*- coding: utf-8 -*-
# @File    : openGL_widget.py
# 功能：
# @Time    : 2023/5/17 9:16
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QOpenGLWidget,QTreeWidget,QApplication
from PyQt5.QtGui import QOpenGLVersionProfile, QPainter, QMouseEvent, QColor,QImage
from PyQt5.QtCore import Qt
import sys


class OpenGlWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.map = None
        self.gl = None
        # self.image = QImage()  # 用于存储图像
        self.offset = (0, 0)  # 图像的偏移量
        self.scale = 0.1
        # self.last_pos = None  # 上次鼠标位置#
        # self.image.load("E:\qt\qt_python\pyqt_test\input\image.PNG")

    def initializeGL(self):
        """初始化 opengl窗口部件"""
        version_profile = QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl = self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()

        self.gl.glClearColor(1.0,1.0,1.0,1.0)  # 清除屏幕所用颜色
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)  # 启用深度测试
        print("init opengl")

    def paintGL(self):
        """绘制opengl窗口"""
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT|self.gl.GL_DEPTH_BUFFER_BIT)  # 清楚屏幕和深度缓存
        self.gl.glLoadIdentity()  ## 重置当前的模型观察矩阵
        # self.gl.glOrtho(-180 * self.scale + self.offset[0], 180 * self.scale + self.offset[0],
        #         -90 * self.scale + self.offset[1], 90 * self.scale + self.offset[1], -1, 1)
        self.gl.glOrtho(-180 * self.scale + self.offset[0], 180 * self.scale + self.offset[0],
                -90 * self.scale + self.offset[1], 90 * self.scale + self.offset[1], -1, 1)
        self.gl.glBegin(self.gl.GL_TRIANGLES)  # 开始绘制三角形

        self.gl.glColor3d(1.0,0.0,0.0)  # 上色
        self.gl.glVertex3d(0.0,1.0,1.0)  # 放置点，x,y,z
        self.gl.glColor3d(0.0,1.0,0.0)
        self.gl.glVertex3d(-1.0,-1.0,1.0)
        self.gl.glColor3d(0.0,0.0,1.0)
        self.gl.glVertex3d(1.0,-1.0,1.0)
        self.gl.glEnd()
        self.gl.glBegin(self.gl.GL_LINES)
        self.gl.glVertex3d(-1.5, -1.5, 0)
        self.gl.glVertex3d(1.5, 1.5, 0)
        self.gl.glEnd()  # 结束画点
    #
    #     painter = QPainter(self)
    #     painter.beginNativePainting()
    #
    #     # 清除画布
    #     painter.fillRect(0, 0, self.width(), self.height(), Qt.white)
    #
    #     # 绘制图像
    #     painter.drawImage(self.offset[0], self.offset[1], self.image)
    #
    #     painter.endNativePainting()
    #     painter.end()


    def resizeGL(self, width: int, height: int):
        """处理窗口大小"""
        side = min(width, height)
        if side < 0:
            return
        # 重置当前视口
        self.gl.glViewport((width - side) // 2, (height - side) // 2, side, side)
        # 选择投影矩阵
        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        # 重置投影矩阵
        self.gl.glLoadIdentity()
        # 正交投射
        self.gl.glOrtho(-1.5,1.5,-1.5,1.5,-10,10)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    # 鼠标事件
    # def mousePressEvent(self, event: QMouseEvent):
    #     "鼠标点击事件"
    #     if event.button() == Qt.LeftButton:
    #         self.last_pos = event.pos()
    #
    # def mouseMoveEvent(self, event: QMouseEvent):
    #     """鼠标移动"""
    #     if event.buttons() == Qt.LeftButton and self.last_pos:
    #         # 计算鼠标的偏移量
    #         dx = event.pos().x() - self.last_pos.x()
    #         dy = event.pos().y() - self.last_pos.y()
    #
    #         # 更新图像的偏移量
    #         self.offset = (self.offset[0] + dx, self.offset[1] + dy)
    #         self.update()
    #
    #         # 更新鼠标位置
    #         self.last_pos = event.pos()
    #
    # def mouseReleaseEvent(self, event: QMouseEvent):
    #     if event.button() == Qt.LeftButton:
    #         self.last_pos = None




if __name__ == "__main__":
    app = QApplication(sys.argv)


    pp = OpenGlWidget()
    pp.show()
    sys.exit(app.exec_())
