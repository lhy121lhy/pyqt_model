# -*- coding: utf-8 -*-
# @File    : tt2.py
# 功能：
# @Time    : 2023/5/24 8:59
# @Author  : lhy
# @Software: PyCharm


from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView,QGraphicsItem
from PyQt5.QtCore import Qt, QPointF,QRectF
from PyQt5.QtGui import QPainter, QPen



class DraggableItem(QGraphicsItem):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget):
        painter.drawRect(self.rect)


class TranslateData:
    def __init__(self):
        self.last_mouse_pos = None
        self.offset = QPointF(0, 0)


if __name__ == '__main__':
    app = QApplication([])
    scene = QGraphicsScene()
    view = QGraphicsView(scene)
    view.resize(400, 300)

    # 在场景中添加可拖拽的图元
    item1 = DraggableItem(QRectF(50, 50, 100, 100))
    item2 = DraggableItem(QRectF(200, 200, 100, 100))
    scene.addItem(item1)
    scene.addItem(item2)

    # 定义平移偏移量
    translate_data = TranslateData()

    def translate_view():
        # 平移视图
        view.translate(translate_data.offset.x(), translate_data.offset.y())

        # 平移所有图元
        for item in scene.items():
            item.setPos(item.pos() + translate_data.offset)

    def handle_mouse_move(event):
        if event.buttons() == Qt.LeftButton:
            if translate_data.last_mouse_pos:
                # 计算鼠标移动的偏移量
                current_pos = event.pos()
                last_pos = translate_data.last_mouse_pos
                translate_data.offset = view.mapToScene(current_pos) - view.mapToScene(last_pos)
                translate_view()

            translate_data.last_mouse_pos = event.pos()

    def handle_mouse_release(event):
        if event.button() == Qt.LeftButton:
            translate_data.last_mouse_pos = None

    view.mouseMoveEvent = handle_mouse_move
    view.mouseReleaseEvent = handle_mouse_release

    view.show()
    app.exec_()