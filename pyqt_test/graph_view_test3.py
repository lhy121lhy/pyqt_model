# -*- coding: utf-8 -*-
# @File    : graph_view_test3.py
# 功能：
# @Time    : 2023/5/20 22:45
# @Author  : lhy
# @Software: PyCharm

from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene,QGraphicsLineItem
from PyQt5.QtGui import QPainter, QPen,QBrush,QTransform,QDrag
from PyQt5.QtCore import Qt, QPointF,QRectF,QLineF,QMimeData


class MyView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene_c = QGraphicsScene(self)
        self.setGeometry(0,0,1200,800)
        self.setScene(self.scene_c)
        self.setRenderHint(QPainter.Antialiasing)
        self.offset = (0, 0)
        # self.scene_c.setSceneRect(QRectF(self.offset[0],self.offset[1],100.0,100.0))
        self.scene_c.setSceneRect(QRectF(-self.width()/2, -self.height()/2, self.width()/2, self.height()/2))
        self.data_gis = [QLineF(-1205.0,-805.0,0,0)]
            # ,QLineF(1.0,50.0,80.0,15.0),
            #              QLineF(0,0,80.0,85.0)]

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransform(QTransform().scale(1.0, 1.0))
        # self.setTransformationAnchor(QGraphicsView.AnchorViewCenter)
        # self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # self.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.viewport().setMouseTracking(True)
        # self.viewport().installEventFilter(self)

        self.mouse_press_pos = None
        self.drawLines()


    def up_date_line(self):
        for item in self.scene_c.items():  # 更新每个图元
            item.update()

    def drawLines(self):
        pen = QPen()
        pen.setColor(Qt.red)

        for line in self.data_gis:
            _line = QGraphicsLineItem()
            _line.setLine(line)
            _line.setPen(pen)
            self.scene_c.addItem(_line)

    def wheelEvent(self, event):
        # 处理鼠标滚轮事件，实现图片的放大和缩小
        print("鼠标滚轮")
        zoom_factor = 0.1  # 缩放因子
        if event.angleDelta().y() > 0:
            # 鼠标向前滚动，进行放大操作
            self.scale(1 + zoom_factor, 1 + zoom_factor)
        else:
            # 鼠标向后滚动，进行缩小操作
            self.scale(1 - zoom_factor, 1 - zoom_factor)

    def mousePressEvent(self, event):
        # 处理鼠标按下事件，记录鼠标按下的初始位置
        print("按下左键",self.width(), self.height())
        # 场景坐标和本地坐标
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.pos()
            print("view坐标", self.mouse_press_pos)
            print("scene坐标", self.mapToScene(self.mouse_press_pos))
            print("图元坐标",self.mapFromScene(self.mapToScene(self.mouse_press_pos)))
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # 处理鼠标移动事件，计算鼠标的偏移量并进行图片平移
        print("鼠标平移:", self.mouse_press_pos)
        if event.buttons() == Qt.LeftButton and self.mouse_press_pos is not None:
            # 计算鼠标的偏移量
            print("平移后的坐标",event.pos())
            scen_pres = self.mapToScene(self.mouse_press_pos)
            sce_now = self.mapToScene(event.pos())
            delta = sce_now - scen_pres
            dx = event.pos().x() - self.mouse_press_pos.x()
            dy = event.pos().y() - self.mouse_press_pos.y()

            for item in self.scene_c.items():
                # item.moveBy(dx, dy)  # 移动图元自身
                print("old",item.x())
                # item.setPos(item.x() + dx, item.y() + dy)
                item.setPos(item.x()+delta.x(),item.y()+delta.y())
                print("new",item.x())
            #
            # print("图片进行平移,视图位移", dx, dy)
            # print("图片进行平移,场景位移", delta.x(),delta.y())
            # self.mouse_press_pos = event.pos()
            # self.mouse_press_pos = None
            # self.translate(delta.x(),delta.y())
            self.mouse_press_pos = event.pos()
            self.update()
            self.scene_c.update()
            # self.up_date_line()


        # super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件，重置鼠标按下的初始位置
        print("释放左键",event.pos())
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = None



if __name__ == '__main__':
    app = QApplication([])
    view = MyView()
    view.show()
    app.exec_()