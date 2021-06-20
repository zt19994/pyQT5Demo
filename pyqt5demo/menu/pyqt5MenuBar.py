#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 16:49
# @Author  : zt

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 创建一个菜单栏和一个菜单。这个菜单将终止应用程序。Ctrl + Q的行动是可访问的快捷方式。
        # QAction可以操作菜单栏,工具栏,或自定义键盘快捷键。
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        # 创建一个鼠标指针悬停在该菜单项上时的提示
        exitAction.setStatusTip('Exit application')
        # 点击菜单的时候，调用qApp.quit,终止应用程序
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)
        # 设置窗口大小
        self.setGeometry(300, 300, 300, 200)
        # 设置窗口的标题
        self.setWindowTitle('Menubar')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
