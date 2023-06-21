# -*- coding: utf-8 -*-
# @File    : main_window.py
# 功能：窗口界面设计
# @Time    : 2023/5/16 21:10
# @Author  : lhy
# @Software: PyCharm
import sys
import write_log
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QWidget,QHBoxLayout,QVBoxLayout,QTabWidget
from widget_mw.layer_tree_widget import LayerTreeWidget
from widget_mw.openGL_widget import OpenGlWidget
from widget_mw.toolbox_treewidget import toolbox_tree_widget
from widget_mw.graphview_widget import GraphViewWidget
from utools.open_tools import read_shp_file, OpenFile
from utools.parameter_set import ProjectSeting
import logging
from geometry_data.geo_map import GeoMap
from window_ui.menus import QtMenusBox


class MainWindowUi(QMainWindow):
    def __init__(self,):
        super().__init__()
        # 变量定义
        self.center_widget = QWidget()
        self.geo_map = GeoMap()

        # 控件
        self.layers_widget = LayerTreeWidget()
        self.toolbox_widget = toolbox_tree_widget()
        self.graphview_widget = GraphViewWidget()
        self.tab_widget = QTabWidget()

        self.q_menus_box = None  # 菜单
        self.tools_box = None  # 工具
        self.open_tool = OpenFile()
        self.data_parameter = ProjectSeting()


        self.init_window()

    def init_window(self):
        """初始化"""
        logging.info("init windows")
        self.setWindowTitle("MacMd by 天朝宇")
        self.setGeometry(200, 200, 1200, 800)
        self.create_menus_actions()
        self.setup_layout()
        self.signal_slots_connection()

    def create_menus_actions(self):
        """
        创建菜单和操作
        :return:
        """
        # 创建一级菜单
        menubar = self.menuBar()
        tool_box = self.addToolBar("md_tools")

        self.q_menus_box = QtMenusBox(menubar, tool_box)
        self.q_menus_box.file_add_items()  # 添加菜单
        self.q_menus_box.edit_add_items()  # 编辑添加菜单
        self.q_menus_box.add_tool_box()  # 添加工具箱

    def setup_layout(self):
        """页面布局"""
        # self.layers_widget = layer_treewidget()
        # self.layers_widget.setWindowTitle("数据管理窗口")
        # self.toolbox_widget = toolbox_tree_widget()
        # self.opengl_widget = OpenGlWidget()
        # layers_widget = layer_treewidget()
        # toolbox_widget = toolbox_tree_widget()
        # opengl_widget = OpenGlWidget()

        self.setCentralWidget(self.center_widget)
        # self.setCentralWidget(self.tab_widget)

        h_main_layout = QHBoxLayout(self.center_widget)
        v_left_layout = QVBoxLayout()

        h_main_layout.setSpacing(6)
        v_left_layout.addWidget(self.layers_widget)
        v_left_layout.addWidget(self.toolbox_widget)

        h_main_layout.addLayout(v_left_layout)
        # h_main_layout.addWidget(self.opengl_widget)

        self.tab_widget.addTab(self.graphview_widget, "start")
        self.tab_widget.addTab(QWidget(), "second")
        self.tab_widget.addTab(QWidget(), "third")
        # self.tab_widget.setCurrentIndex(0)

        h_main_layout.addWidget(self.tab_widget)

        # self.tab_widget.addTab(self.opengl_widget, "second")

        h_main_layout.setContentsMargins(11, 11, 11, 11)
        h_main_layout.setStretch(0, 0)
        h_main_layout.setStretch(1, 3)
        self.setLayout(h_main_layout)

    def signal_slots_connection(self):
        """信号与槽函数"""
        # self.openAction.triggered.connect(self.open_file)
        # pass
        self.q_menus_box.exitAction.triggered.connect(self.close)
        # self.q_menus_box.openAction.triggered.connect(self.open_tool.open_file)
        self.q_menus_box.openAction.triggered.connect(self.open_data)
        # self.q_menus_box.exitAction.triggered.connect(self.close)

    def update_function(self):
        """
        """
        self.data_parameter.append_data(self.open_tool.file_dict)
        self.graphview_widget.draw_pen(self.data_parameter.data_style)
        self.layers_widget.update_tree(self.data_parameter.data_style)

    def open_data(self):
        # 打开文件对话框
        self.open_tool.open_file()

        self.update_function()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowUi()
    win.show()
    sys.exit(app.exec_())