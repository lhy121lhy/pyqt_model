# -*- coding: utf-8 -*-
# @File    : menus.py
# 功能：
# @Time    : 2023/6/8 9:21
# @Author  : lhy
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QWidget,QHBoxLayout,QVBoxLayout,QTabWidget
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QToolBar,QStyle
from PyQt5.QtGui import QIcon


class QtMenusBox:

    def __init__(self, menubar, tool_box):
        self.menu_bar = menubar
        self.tools_bar = tool_box

        self.file_menu = menubar.addMenu("File")
        self.edit_menu = menubar.addMenu("Edit")
        self.view_menu = menubar.addMenu("View")
        self.tools_menu = menubar.addMenu("Tools")
        self.win_menu = menubar.addMenu("windows")
        self.help_menu = menubar.addMenu("help")

        # 操作
        self.newAction = None
        self.openAction = None
        self.saveAction = None
        self.exitAction = None
        self.undoAction = None
        self.redoAction = None
        self.cutAction = None
        self.copyAction = None
        self.pasteAction = None

    def add_tool_box(self):
        """
        pass
        :return:
        """

        self.tools_bar.addAction(self.newAction)
        self.tools_bar.addAction(self.openAction)
        self.tools_bar.addAction(self.saveAction)
        self.tools_bar.addAction(self.exitAction)

        self.tools_bar.addSeparator()
        self.tools_bar.addAction(self.undoAction)
        self.tools_bar.addAction(self.redoAction)
        # self.tools_bar.addSeparator()
        self.tools_bar.addAction(self.cutAction)
        self.tools_bar.addAction(self.copyAction)
        self.tools_bar.addAction(self.pasteAction)

    def file_add_items(self):
        """
        :return:
        """
        # 创建二级菜单
        im_menu = QMenu("New")
        self.file_menu.addMenu(im_menu)

        # 添加菜单项
        self.newAction = QAction(QIcon("src_img/new.PNG"), "New")
        self.newAction.setShortcut("Ctrl+N")
        im_menu.addAction(self.newAction)

        #QIcon(QApplication.style().standardIcon(QStyle.SP_DirClosedIcon))
        # self.openAction = QAction(QIcon("src_img/open.PNG"), "Open")
        self.openAction = QAction(QIcon(QApplication.style().standardIcon(QStyle.SP_DirClosedIcon)), "Open")

        self.openAction.setShortcut("Ctrl+O")
        self.file_menu.addAction(self.openAction)

        self.saveAction = QAction(QIcon("src_img/save.PNG"), "Save")
        self.saveAction.setShortcut("Ctrl+S")
        self.file_menu.addAction(self.saveAction)

        self.exitAction = QAction(QIcon("src_img/exit.PNG"), "Exit")
        self.exitAction.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.exitAction)

    def edit_add_items(self):
        """
        :return:
        """
        # 创建二级菜单

        self.undoAction = QAction(QIcon("src_img/undo.PNG"), "Undo")
        self.undoAction.setShortcut("Ctrl+Z")
        self.edit_menu.addAction(self.undoAction)

        self.redoAction = QAction(QIcon("src_img/redo.PNG"), "Redo")
        self.redoAction.setShortcut("Ctrl+Y")
        self.edit_menu.addAction(self.redoAction)

        self.cutAction = QAction(QIcon("src_img/cut.PNG"), "Cut")
        self.cutAction.setShortcut("Ctrl+X")
        self.edit_menu.addAction(self.cutAction)

        self.copyAction = QAction(QIcon("src_img/copy.PNG"), "Copy")
        self.copyAction.setShortcut("Ctrl+C")
        self.edit_menu.addAction(self.copyAction)

        self.pasteAction = QAction(QIcon("src_img/paste.PNG"), "Paste")
        self.pasteAction.setShortcut("Ctrl+V")
        self.edit_menu.addAction(self.pasteAction)

    def view_add_items(self):
        """
        :return:
        """
        # 创建二级菜单
        self.saveAction = QAction(QIcon("src_img/save.PNG"), "Find", self)
        self.saveAction.setShortcut("Ctrl+F")
        self.view_menu.addAction(self.saveAction)

    def tools_add_items(self):
        """
        :return:
        """
        # 添加菜单项
        self.newAction = QAction(QIcon("src_img/new.PNG"), "Tools", self)
        self.newAction.setShortcut("Ctrl+T")
        self.tools_menu.addAction(self.newAction)

    def windows_add_items(self):
        """
        :return:
        """
        # 创建二级菜单
        pass

    def find_add_items(self):
        """
        :return:
        """
        # 创建二级菜单
        pass


