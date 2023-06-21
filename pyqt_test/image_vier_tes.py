# -*- coding: utf-8 -*-
# @File    : image_vier_tes.py
# 功能：
# @Time    : 2023/5/20 22:31
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QMainWindow
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap,QTransform


class ImageViewer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Image Viewer')

        # 创建 QGraphicsView 和 QGraphicsScene
        self.graphics_view = QGraphicsView()
        self.graphics_scene = QGraphicsScene()
        # self.graphics_scene.setSceneRect()

        # 创建 QGraphicsPixmapItem 并添加到 QGraphicsScene 中
        self.pixmap_item = QGraphicsPixmapItem()
        self.graphics_scene.addItem(self.pixmap_item)

        # 设置 QGraphicsScene 到 QGraphicsView
        self.graphics_view.setScene(self.graphics_scene)

        # 设置视口大小策略和滚动条策略
        self.graphics_view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 设置初始缩放比例
        self.graphics_view.setTransform(QTransform().scale(1.0, 1.0))

        # 设置主窗口的中央部件为 QGraphicsView
        self.setCentralWidget(self.graphics_view)

        # 加载并显示图片
        self.load_image('E:\qt\qt_python\pyqt_test\input\image.PNG')

        # 保存鼠标按下的初始位置
        self.mouse_press_pos = None

    def load_image(self, filepath):
        pixmap = QPixmap(filepath)
        # self.pixmap_item.setPos(-10,-10)  # 设置位置为 (100, 100)
        self.pixmap_item.setPixmap(pixmap)

    def wheelEvent(self, event):
        factor = 1.2 ** (event.angleDelta().y() / 120)
        print("wheelEvent")
        self.scale(factor, factor)
        self.update()

    def mousePressEvent(self, event):
        # 处理鼠标按下事件，记录鼠标按下的初始位置
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.pos()
            print("1",self.mouse_press_pos)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # 处理鼠标移动事件，计算鼠标的偏移量并进行图片平移
        if event.button() == Qt.LeftButton and self.mouse_press_pos is not None:
            # 计算鼠标的偏移量
            offset = event.pos() - self.mouse_press_pos
            # 进行图片平移
            self.graphics_view.translate(offset.x(), offset.y())
        print("3")
        super().mouseMoveEvent(event)
        self.repaint()

    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件，重置鼠标按下的初始位置
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = None
        print("2",event.pos())
        super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    window = ImageViewer()
    window.show()
    app.exec_()
