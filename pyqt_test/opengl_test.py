# -*- coding: utf-8 -*-
# @File    : opengl_test.py
# 功能：
# @Time    : 2023/5/18 15:25
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtGui import QPainter,QMouseEvent
from PyQt5.QtCore import Qt,QPointF
from pyproj import Proj, transform,CRS
from OpenGL.GL import *
import sys
import shapefile
import geopandas as gpd
import warnings
warnings.filterwarnings("ignore",category=Warning)

class MyOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vertices = []
        self.translation = QPointF(0.0, 0.0)
        self.scale = 1.0

    def initializeGL(self):

        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-180, 180, -90, 90, -1, 1)
        # glOrtho(-100000 * self.scale + self.translation.x(), 100000 * self.scale + self.translation.x(),
        #         -100000 * self.scale + self.translation.y(), 100000 * self.scale + self.translation.y(), -1.0, 1.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_STRIP)
        for vertex in self.vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()
        # update()

    def load_shpfile(self, filepath):
        gpd_shp = gpd.read_file(filepath)
        gpd_shp_cr = gpd_shp.to_crs(crs='EPSG:2381')
        min_coor = 0
        max_coor = 100000
        for geo_s in gpd_shp_cr.geometry:
            for point in list(geo_s.exterior.coords):

                self.vertices.append(((point[0]-(max_coor-min_coor))/max_coor,
                                      (point[1]-(max_coor-min_coor))/max_coor))


        # sf = shapefile.Reader(filepath)
        # shapes = sf.shapes()
        # # src_proj = Proj(sf.shapeTypeName())
        # dst_proj = Proj(proj='latlong', datum='WGS84')
        # crs_WGS84 = CRS.from_epsg(4326)  # WGS84地理坐标系
        # crs_WebMercator = CRS.from_epsg(3857)  # Web墨卡托投影坐标系
        # for shape in shapes:
        #     for point in shape.points:
        #         # 坐标转换
        #         lon, lat = transform(crs_WGS84, crs_WebMercator, point[0], point[1])
        #         self.vertices.append((lon, lat))
        # shapes = sf.shapes()
        # for shape in shapes:
        #     for point in shape.points:
        #         self.vertices.append(point)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenGL SHP Demo")
        self.setGeometry(100, 100, 800, 600)

        self.openGLWidget = MyOpenGLWidget(self)
        self.setCentralWidget(self.openGLWidget)
        self.openGLWidget.load_shpfile("E:\qt\qt_python\pyqt_test\input\shp\杭州交通小区（初版）.shp")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
