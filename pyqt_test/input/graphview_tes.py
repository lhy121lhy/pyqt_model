# -*- coding: utf-8 -*-
# @File    : graphview_tes.py
# 功能：
# @Time    : 2023/5/18 20:28
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene,QGraphicsPolygonItem,QLabel
from PyQt5.QtGui import QPen, QColor,QPolygonF,QMouseEvent,QPainter
from shapely.geometry import shape
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import shapefile
from PyQt5.QtCore import QPointF
import geopandas as gpd
from PyQt5.QtCore import Qt

x = [-20037508.3427892,20037508.3427892]
y = [-20037508.3427892,20037508.3427892]


class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene())
        self.setDragMode(QGraphicsView.ScrollHandDrag)  # 设置拖拽模式为滚动手柄拖拽
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)  # 设置变换锚点为鼠标位置
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)  # 设置调整大小锚点为鼠标位置
        self.coordinates_label = QLabel(self)  # 创建一个标签用于显示坐标
        self.coordinates_label.setStyleSheet("background-color: white; padding: 5px;")
        self.coordinates_label.setFixedSize(10, 30)
        self.coordinates_label.setMouseTracking(False)  # 禁用鼠标跟踪，只在鼠标按下时显示坐标

        # self.setSceneRect(x[0], y[0], x[1]-x[0], y[1]-y[0])
        self.setSceneRect(-200, -200, 200, 200)
        self.last_pos = None
        self.is_mouse_pressed = False  # 记录鼠标左键是否按下


    def drawline(self):
        pen = QPen(QColor(0, 0, 0))
        tPolygon = QPolygonF([QPointF(-200,-320),QPointF(0,0),QPointF(40,50),QPointF(10,38),QPointF(20,280)])
        polygon = QGraphicsPolygonItem()
        polygon.setPolygon(tPolygon)
        polygon.setPen(pen)
        # polygon.setPos()
        self.scene().addItem(polygon)


    def drawShape(self, shpfile):
        pen = QPen(QColor(0, 0, 0))
        with shapefile.Reader(shpfile) as sf:
            for shape_record in sf.shapeRecords():
                geom = shape(shape_record.shape.__geo_interface__)
                # 根据具体的几何类型进行绘制操作，这里以Polygon为例
                if geom.geom_type == 'Polygon':
                    polygon = QGraphicsPolygonItem()
                    polygon.setPolygon(self.convertPolygon(geom))
                    polygon.setPen(pen)
                    # polygon.setPos()
                    self.scene().addItem(polygon)



    @staticmethod
    def convertPolygon(geom):
        exterior = geom.exterior.coords[:]
        interior = [i.coords[:] for i in geom.interiors]
        polygon = QPolygonF()
        for point in exterior:
            qpoint = QPointF(point[0], point[1])
            polygon.append(qpoint)
        # for interior_ring in interior:
        #     ring = QPolygonF()
        #     for point in interior_ring:
        #         qpoint = QPointF(point[0], point[1])
        #         ring.append(qpoint)
        #
        #     polygon.append(ring)
        return polygon

    def wheelEvent(self, event):
        # 处理滚轮事件，实现缩放功能
        factor = 1.2 ** (event.angleDelta().y() / 120)  # 计算缩放因子
        self.scale(factor, factor)

    def mousePressEvent(self, event):
        # 处理鼠标按下事件，记录鼠标按下时的位置
        if event.buttons() == Qt.LeftButton:
            self.last_pos = event.pos()
        # self.coordinates_label.move(event.globalPos() + QPointF(10, 10))  # 设置标签的位置
        # self.coordinates_label.setText("")  # 清空标签的文本
        # self.coordinates_label.show()  # 显示标签

    def mouseMoveEvent(self, event):
        # 处理鼠标移动事件，计算鼠标移动的偏移量并进行平移
        # if self.is_mouse_pressed:
        if event.buttons() == Qt.LeftButton:
        # self.last_pos = event.pos()
            dx = event.x() - self.last_pos.x()
            dy = event.y() - self.last_pos.y()
            self.translate(dx, dy)
            self.last_pos = event.pos()
            # 将视图坐标转换为场景坐标
            # scene_pos = self.mapToScene(event.pos())
            # self.coordinates_label.setText(f"X: {scene_pos.x()}, Y: {scene_pos.y()}")  # 更新标签文本

    def translate(self, dx, dy):
        # 实现平移功能
        transform = self.transform()  # 获取当前的变换矩阵
        transform.translate(dx, dy)  # 在x和y方向上平移
        self.setTransform(transform)  # 应用变换矩阵



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = MyGraphicsView()
        self.setCentralWidget(self.view)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Shpfile Visualization")

        # 绘制shpfile
        # self.view.drawShape('E:\qt\qt_python\pyqt_test\input\shp\杭州交通小区（初版）.shp')
        self.view.drawline()




def read_shp_file(shp_file):
    #
    geo_data = gpd.read_file(shp_file, encodings="gbk").to_crs("EPSG:3857")
    return geo_data



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
