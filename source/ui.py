# -*- coding: utf-8 -*-
# @File    : ui.py
# 功能：
# @Time    : 2023/4/13 16:06
# @Author  : lhy
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QAction, QFileDialog
from PyQt5.QtGui import QPen, QColor, QBrush, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, QPointF, QRectF


class RoadNetworkEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("道路网络编辑器")
        self.setGeometry(100, 100, 800, 600)

        # 创建场景和视图
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 800, 600)

        # 创建画笔和画刷
        self.pen = QPen(QColor(0, 0, 0), 2, Qt.SolidLine)
        self.brush = QBrush(QColor(255, 255, 255), Qt.SolidPattern)

        # 创建道路网络节点和边
        self.nodes = []
        self.edges = []

        # 创建菜单栏和工具栏
        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        # 创建文件菜单
        file_menu = self.menuBar().addMenu("文件")

        # 创建打开文件动作
        open_action = QAction("打开", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # 创建保存文件动作
        save_action = QAction("保存", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

    def create_toolbar(self):
        # 创建工具栏
        toolbar = self.addToolBar("工具栏")

        # 创建添加节点动作
        add_node_action = QAction("添加节点", self)
        add_node_action.triggered.connect(self.add_node)
        toolbar.addAction(add_node_action)

        # 创建添加边动作
        add_edge_action = QAction("添加边", self)
        add_edge_action.triggered.connect(self.add_edge)
        toolbar.addAction(add_edge_action)

    def open_file(self):
        # 打开文件对话框
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "道路网络文件 (*.rnw)")

        # 读取文件内容并更新场景
        if file_name:
            with open(file_name, "r") as f:
                for line in f:
                    if line.startswith("node"):
                        parts = line.strip().split(",")
                        x, y = float(parts[1]), float(parts[2])
                        self.add_node(QPointF(x, y))
                    elif line.startswith("edge"):
                        parts = line.strip().split(",")
                        start_node = self.nodes[int(parts[1])]
                        end_node = self.nodes[int(parts[2])]
                        self.add_edge(start_node, end_node)

    def save_file(self):
        # 打开文件对话框
        file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "道路网络文件 (*.rnw)")

        # 写入文件内容
        if file_name:
            with open(file_name, "w") as f:
                for i, node in enumerate(self.nodes):
                    f.write("node,{},{},{}\n".format(i, node.pos().x(), node.pos().y()))
                for edge in self.edges:
                    start_node = self.nodes.index(edge.start_node)
                    end_node = self.nodes.index(edge.end_node)
                    f.write("edge,{},{},{}\n".format(start_node, end_node, edge.weight))

    def add_node(self, pos=None):
        # 创建节点并添加到场景和节点列表中
        node = RoadNetworkNode(pos or self.view.mapToScene(self.view.viewport().rect().center()))
        self.scene.addItem(node)
        self.nodes.append(node)

    def add_edge(self, start_node=None, end_node=None):
        # 如果没有指定起始节点和结束节点，则让用户选择
        if not start_node or not end_node:
            selected_items = self.scene.selectedItems()
            if len(selected_items) == 2 and isinstance(selected_items[0], RoadNetworkNode) and isinstance(selected_items[1], RoadNetworkNode):
                start_node, end_node = selected_items
            else:
                return

        # 创建边并添加到场景和边列表中
        edge = RoadNetworkEdge(start_node, end_node)
        self.scene.addItem(edge)
        self.edges.append(edge)

    def keyPressEvent(self, event: QKeyEvent):
        # 如果按下 Delete 键，则删除选中的节点和边
        if event.key() == Qt.Key_Delete:
            for item in self.scene.selectedItems():
                if isinstance(item, RoadNetworkNode):
                    self.nodes.remove(item)
                elif isinstance(item, RoadNetworkEdge):
                    self.edges.remove(item)
                self.scene.removeItem(item)

    def mousePressEvent(self, event: QMouseEvent):
        # 如果按下 Ctrl 键，则添加节点
        if event.modifiers() == Qt.ControlModifier:
            self.add_node(event.scenePos())
        # 如果按下 Shift 键，则添加边
        elif event.modifiers() == Qt.ShiftModifier:
            self.add_edge()

class RoadNetworkNode(QGraphicsItem):
    def __init__(self, pos):
        super().__init__()

        # 设置节点位置和大小
        self.pos = pos
        self.rect = QRectF(-10, -10, 20, 20)

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget=None):
        # 绘制节点
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 0, 0))
        painter.drawEllipse(self.rect)

    def pos(self):
        return self.pos

class RoadNetworkEdge(QGraphicsItem):
    def __init__(self, start_node, end_node):
        super().__init__()

        # 设置起始节点、结束节点和边权重
        self.start_node = start_node
        self.end_node = end_node
        self.weight = 1

    def boundingRect(self):
        # 计算边的矩形范围
        start_pos = self.start_node.pos()
        end_pos = self.end_node.pos()
        x = min(start_pos.x(), end_pos.x())
        y = min(start_pos.y(), end_pos.y())
        w = abs(start_pos.x() - end_pos.x())
        h = abs(start_pos.y() - end_pos.y())
        return QRectF(x, y, w, h)

    def paint(self, painter, option, widget=None):
        # 绘制边
        painter.setPen(QPen(QColor(0, 0, 255), 2, Qt.SolidLine))
        painter.drawLine(self.start_node.pos(), self.end_node.pos())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = RoadNetworkEditor()
    editor.show()
    sys.exit(app.exec_())