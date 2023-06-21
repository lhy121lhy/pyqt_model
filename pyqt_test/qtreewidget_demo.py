# -*- coding: utf-8 -*-
# @File    : qtreewidget_demo.py
# 功能：
# @Time    : 2023/5/19 14:51
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QCheckBox
from PyQt5.QtCore import Qt,QPointF


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setColumnCount(1)
        self.tree_widget.setHeaderLabels(["数据显示管理窗口"])
        self.setCentralWidget(self.tree_widget)

        self.populate_tree()

    def populate_tree(self):
        # 添加根节点
        root = QTreeWidgetItem(self.tree_widget)
        root.setFlags(root.flags() | Qt.ItemIsUserCheckable)
        root.setText(0, "Layers")

        # 添加子节点
        child1 = QTreeWidgetItem(root)
        child1.setFlags(child1.flags() | Qt.ItemIsUserCheckable)  # 设置标志以允许用户选择
        child1.setCheckState(0, Qt.Unchecked)  # 设置初始复选框状态为未选中
        child1.setText(0, "Child 1")

        child2 = QTreeWidgetItem(root)
        child2.setFlags(child2.flags() | Qt.ItemIsUserCheckable)
        child2.setCheckState(0, Qt.Unchecked)
        child2.setText(0, "Child 2")

        # 添加子节点的子节点
        subchild = QTreeWidgetItem(child2)
        subchild.setFlags(subchild.flags() | Qt.ItemIsUserCheckable)
        subchild.setCheckState(0, Qt.Unchecked)
        subchild.setText(0, "Subchild")

    def show_window(self):
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show_window()
    app.exec_()
