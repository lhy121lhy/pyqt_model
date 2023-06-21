# -*- coding: utf-8 -*-
# @File    : qt_test.py
# 功能：
# @Time    : 2023/4/17 15:12
# @Author  : lhy
# @Software: PyCharm
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *
import shapefile


class ShapefileEditor(QWidget):
    def __init__(self):
        super().__init__()

        # 创建Shapefile对象
        self.shp = shapefile.Reader('test.shp')

        # 创建PyQt窗口
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Shapefile Editor')

        # 创建OpenGL视图
        self.glWidget = GLWidget()

        # 创建操作按钮
        openBtn = QPushButton('Open')
        openBtn.clicked.connect(self.openFile)
        saveBtn = QPushButton('Save')
        saveBtn.clicked.connect(self.saveFile)
        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.addFeature)

        # 创建按钮布局
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(openBtn)
        btnLayout.addWidget(saveBtn)
        btnLayout.addWidget(addBtn)

        # 创建主布局
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.glWidget)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)

    # 打开Shapefile
    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open shapefile',
                                                  'c:\\', '*.shp')
        if filename:
            self.shp = shapefile.Reader(filename)
            self.glWidget.update()

    # 保存Shapefile
    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save shapefile',
                                                  'c:\\', '*.shp')
        self.shp.write(filename)

    # 添加要素
    def addFeature(self):
        pass  # TODO


# OpenGL视图窗口
class GLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.shp = None

    # 初始化OpenGL
    def initializeGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)

    # 绘制场景
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.shp:
            for shape in self.shp.shapes():
                glBegin(GL_LINE_LOOP)
                for x, y in shape.points:
                    glVertex2f(x, y)
                glEnd()

    # 更新视图
    def update(self):
        self.shp = self.parent().shp  # 获取Shapefile数据
        self.update()  # 更新视图


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ShapefileEditor()
    editor.show()
    sys.exit(app.exec_())