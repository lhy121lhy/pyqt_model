# -*- coding: utf-8 -*-
# @File    : graphview_t2.py
# 功能：
# @Time    : 2023/5/20 16:50
# @Author  : lhy
# @Software: PyCharm

from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QMainWindow,QGraphicsItem
from PyQt5.QtCore import Qt, QPointF,QRectF,QEvent
from PyQt5.QtGui import QPixmap, QTransform,QMouseEvent


class ImageViewer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Image Viewer')
        # self.setGeometry(0,0,1200,800)
        self.m_pos = None
        self.pressedPos = None
        self.startPos = None
        self.dx = 100.0
        self.dy = 100.0

        # 创建 QGraphicsView 和 QGraphicsScene
        self.graphics_view = QGraphicsView()
        # self.graphics_view.setGeometry(0,0,1200,800)
        self.graphics_scene = QGraphicsScene()
        # self.graphics_scene.setSceneRect(QRectF(0,0,1200,800))
        # self.graphics_v

        # 创建 QGraphicsPixmapItem 并添加到 QGraphicsScene 中
        self.pixmap_item = QGraphicsPixmapItem()
        self.pixmap_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.graphics_scene.addItem(self.pixmap_item)


        # 设置 QGraphicsScene 到 QGraphicsView
        self.graphics_view.setScene(self.graphics_scene)
        self.graphics_view.setOptimizationFlag(True)

        # 设置视口大小策略和滚动条策略
        self.graphics_view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphics_view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphics_view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.graphics_view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphics_view.setMouseTracking(True)
        # self.graphics_view.viewport().installEventFilter(self)
        # self.graphics_view.installEventFilter(self)

        # 设置初始缩放比例
        self.graphics_view.setTransform(QTransform().scale(1.0, 1.0))

        self.setMouseTracking(True)

        # 设置主窗口的中央部件为 QGraphicsView
        self.setCentralWidget(self.graphics_view)
        # self.setMouseTracking(True)

        # 加载并显示图片
        self.load_image('E:\qt\qt_python\pyqt_test\input\image.PNG')

        # 保存鼠标按下的初始位置
        self.mouse_press_pos = None

    def load_image(self, filepath):
        pixmap = QPixmap(filepath)
        self.pixmap_item.setPos(QPointF(self.dx,self.dy))
        self.pixmap_item.setPixmap(pixmap)

    def eventFilter(self, obj, event):
        if obj == self.graphics_view:
            if event.type() == QEvent.MouseMove:
                # 处理鼠标移动事件
                print("mouse move")
                print(event.pos())
        print("eventFilter",obj)
        return False  # 继续传递事件


    def wheelEvent(self, event):
        # 处理鼠标滚轮事件，实现图片的放大和缩小
        print("鼠标滚轮")
        zoom_factor = 0.1  # 缩放因子
        if event.angleDelta().y() > 0:
            # 鼠标向前滚动，进行放大操作
            self.graphics_view.scale(1 + zoom_factor, 1 + zoom_factor)
        else:
            # 鼠标向后滚动，进行缩小操作
            self.graphics_view.scale(1 - zoom_factor, 1 - zoom_factor)

    def mousePressEvent(self, event):
        # 处理鼠标按下事件，记录鼠标按下的初始位置
        print("按下鼠标键",event.button())
        # 场景坐标和本地坐标
        # scenePos = event.scenePos()
        # pos = event.pos()
        # m_pos = pos
        # pressedPos = scenePos
        # startPos = self.pos()
        # event.accept()

        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # 处理鼠标移动事件，计算鼠标的偏移量并进行图片平移
        print("鼠标平移:", self.mouse_press_pos,Qt.LeftButton)
        # scenePos = event.scenePos()
        # pos = event.pos()
        #
        # xInterval = scenePos.x() - self.pressedPos.x()
        #
        # yInterval = scenePos.y() -  self.pressedpos.y()
        #
        # self.setPos(self.startPos + QPointF(xInterval,yInterval))
        # self.update()

        if event.buttons() == Qt.LeftButton and self.mouse_press_pos is not None:
            # 计算鼠标的偏移量
            offset = event.pos() - self.mouse_press_pos
            print("图片进行平移")
            # 进行图片平移
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - offset.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - offset.y())

            # self.graphics_view.translate(offset.x(), offset.y())
        # super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件，重置鼠标按下的初始位置
        print("释放左键")
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = None
        # super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    window = ImageViewer()
    window.show()
    app.exec_()