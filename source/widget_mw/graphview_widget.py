# -*- coding: utf-8 -*-
# @File    : graphview_widget.py
# 功能：
# @Time    : 2023/5/20 19:46
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene,QGraphicsLineItem,QGraphicsPathItem
from PyQt5.QtGui import QPainter, QPen,QBrush,QTransform,QDrag,QPolygonF,QPainterPath
from PyQt5.QtCore import Qt, QPointF,QRectF,QLineF,QMimeData
import sys
from PyQt5.QtOpenGL import QGLWidget

x = [-20037508.3427892,20037508.3427892]
y = [-20037508.3427892,20037508.3427892]

pos_set = [13394977,3562019]

class GraphViewWidget(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene_c = QGraphicsScene(self)
        self.setGeometry(0, 0, 1200, 800)
        self.setScene(self.scene_c)
        # self.setRenderHint(QPainter.Antialiasing)
        # self.setViewport(QGLWidget())

        self.offset = (0, 0)
        # self.scene_c.setSceneRect(QRectF(x[0],y[0],x[1]-x[0],y[1]-y[0]))
        self.scene_c.setSceneRect(QRectF(-self.width() / 2, -self.height() / 2, self.width() / 2, self.height() / 2))

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)  # 允许拖拽
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭横向条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭纵向
        self.setTransform(QTransform().scale(1.0, 1.0))

        # self.data_gis = [QLineF(-1205.0, -805.0, 0, 0)]

        self.mouse_press_pos = None
        # self.drawLines()

    def up_date_line(self,scale):
        # scale = self.transform().m11()
        print("scale",scale)
        for item in self.scene_c.items():  # 更新每个图元
            # item.update()
            # pen_width = min(max(item.pen().widthF() /scale, 0.5), 15)

            item.setPen(QPen(item.pen().color(), item.pen().widthF() /scale))
        # print("new scale",pen_width)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # self.up_date_line()

    def draw_pen(self, data_seting):
        pen = QPen()
        pen.setWidthF(5.0)
        pen.setColor(Qt.red)

        data_index = data_seting["layer_index"]

        for data_id in data_index:
            data_dict = data_seting["data_style"][data_id]
            if data_dict["data_type"] in ["Point"]:
                # "画点"
                pass
            if data_dict["data_type"] in ["LineString"]:
                print("draw linestring")
                line_shp = data_dict["shape"]
                for line in line_shp:
                    polygon = QPolygonF()
                    for index in range(len(line.coords.xy[0])):
                        polygon.append(QPointF(line.coords.xy[0][index]-pos_set[0], -(line.coords.xy[1][index]-pos_set[1])))

                    path = QPainterPath()
                    path.moveTo(polygon[0])
                    for point in polygon:
                        path.lineTo(point)

                    item = QGraphicsPathItem(path)

                    item.setPen(pen)

                    self.scene_c.addItem(item)

            if data_dict["data_type"] in ["Polygon"]:
                pass

        # pen = QPen()
        # pen.setColor(Qt.red)
        #
        # for line in self.data_gis:
        #     _line = QGraphicsLineItem()
        #     _line.setLine(line)
        #     _line.setPen(pen)
        #     self.scene_c.addItem(_line)

    def wheelEvent(self, event):
        # 处理鼠标滚轮事件，实现图片的放大和缩小
        print("鼠标滚轮")
        zoom_factor = 0.1  # 缩放因子
        if event.angleDelta().y() > 0:
            # 鼠标向前滚动，进行放大操作
            self.scale(1 + zoom_factor, 1 + zoom_factor)
            scale = 1 + zoom_factor
        else:
            # 鼠标向后滚动，进行缩小操作
            self.scale(1 - zoom_factor, 1 - zoom_factor)
            scale = 1 - zoom_factor
        self.up_date_line(scale)

    def mousePressEvent(self, event):
        # 处理鼠标按下事件，记录鼠标按下的初始位置
        # print("按下左键")
        # 场景坐标和本地坐标
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.pos()
            # print("view坐标", self.mouse_press_pos)
            # print("scene坐标", self.mapToScene(self.mouse_press_pos))
            # print("图元坐标",self.mapFromScene(self.mapToScene(self.mouse_press_pos)))

    def mouseMoveEvent(self, event):
        # 处理鼠标移动事件，计算鼠标的偏移量并进行图片平移
        # print("鼠标平移:", self.mouse_press_pos)
        if event.buttons() == Qt.LeftButton and self.mouse_press_pos is not None:
            # 计算鼠标的偏移量
            # print("平移后的坐标",event.pos())
            scen_pres = self.mapToScene(self.mouse_press_pos)
            sce_now = self.mapToScene(event.pos())
            delta = sce_now - scen_pres
            for item in self.scene_c.items():
                # item.moveBy(dx, dy)  # 移动图元自身
                item.setPos(item.x()+delta.x(),item.y()+delta.y())
            #     print("new",item.x())

            self.mouse_press_pos = event.pos()
            self.update()
            self.scene_c.update()
            # self.up_date_line()

    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件，重置鼠标按下的初始位置
        # print("释放左键",event.pos())
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = None



if  __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GraphViewWidget()
    win.show()
    win.update()
    sys.exit(app.exec_())