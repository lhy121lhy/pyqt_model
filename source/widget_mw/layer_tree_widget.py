# -*- coding: utf-8 -*-
# @File    : layer_tree_widget.py
# 功能：
# @Time    : 2023/5/16 21:39
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem,QColorDialog
from PyQt5.QtCore import Qt,QRectF,QRect
from PyQt5.QtGui import QIcon,QPainter,QPixmap,QPen


class LayerTreeWidget(QTreeWidget):

    def __init__(self):
        super().__init__()

        self.setHeaderLabel("display manager")
        # self.setWindowTitle("manager")
        # self.header().setStyle()
        # background-color:#83d3ff;
        self.header().setStyleSheet('''QTreewidget {background-color: #DCDCDC;
                                          Color:blue;
                                          font: 16px;
                                          padding: 1px}
                                       QHeaderView::section{
                                                            font:16px; 
                                                            height:36px;  
                                                            font-weight: bold;
                                                            border:1px solid white; 
                                                            
                                                            background-image: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,  
                                                                                           stop: 0.2 rgb(0, 0, 60),  
                                                                                          stop: 0.5 rgb(0, 0, 120),
                                                                                          stop: 0.8 rgb(0, 0, 180), 
                                                                                          stop: 1 rgb(0, 0, 210));
                                                            color:black};''')

        self.tree_item = None

        self.setEditTriggers(QTreeWidget.EditTrigger.EditKeyPressed)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # self.update_tree(None)

    def set_icon(self, shp_type, color=Qt.red, width=1):
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        # 设置画笔属性
        pen = QPen(color)
        pen.setWidth(width)
        painter.setPen(pen)
        # 在指定的区域内画直线
        line_rect = pixmap.rect().adjusted(8, 8, -8, -8)
        painter.drawLine(line_rect.topLeft(), line_rect.bottomRight())
        painter.end()
        icon = QIcon(pixmap)
        return icon

    def update_tree(self, layer_manage):
        """
        更新目录表
        :param layer_manage:
        :return:
        """
        for uid in layer_manage["layer_index"]:
            shp_type = layer_manage["data_style"][uid]["data_type"]
            file_name = layer_manage["data_style"][uid]["layer_name"]

            self.root = QTreeWidgetItem(self)
            self.root.setFlags(self.root.flags() | Qt.ItemIsUserCheckable)
            self.root.setCheckState(0, Qt.Unchecked)
            self.root.setText(0, file_name)
        # self.root.setIcon(0, "src_img/layers.PNG")
            self.root.setIcon(0, self.set_icon(shp_type))

        # 添加子节点
            child1 = QTreeWidgetItem(self.root)
            child1.setFlags(child1.flags() | Qt.ItemIsUserCheckable)  # 设置标志以允许用户选择
            child1.setCheckState(0, Qt.Unchecked)  # 设置初始复选框状态为未选中
            child1.setText(0, "Child 1")

        # child2 = QTreeWidgetItem(child1)
        # child2.setFlags(child2.flags() | Qt.ItemIsUserCheckable)
        # child2.setCheckState(0, Qt.Unchecked)
        # child2.setText(0, "Child 2")
        # for layer in layer_manage:
        #     file_name = layer[1]
        #     child1 = QTreeWidgetItem(self.root)
        #     child1.setFlags(child1.flags() | Qt.ItemIsUserCheckable)  # 设置标志以允许用户选择
        #     child1.setCheckState(0, Qt.Unchecked)  # 设置初始复选框状态为未选中
        #     child1.setText(0, file_name)

    def add_trees(self):
        """PASS"""
        pass

    def show_context_menu(self,pos):
        print('Show context menu')
        item = self.itemAt(pos)
        color = QColorDialog.getColor()
        if color.isValid():
            item.setBackground(0, color)









