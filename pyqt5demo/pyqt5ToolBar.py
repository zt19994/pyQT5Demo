#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 16:57
# @Author  : zt

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.toolbar = self.addToolBar('Exit')
        self.init_ui()

    def init_ui(self):
        # 创建一个简单的工具栏。工具栏有有一个按钮,点击关闭窗口
        exitAction = QAction(QIcon('exit2.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        # 点击菜单的时候，调用qApp.quit,终止应用程序
        exitAction.triggered.connect(qApp.quit)

        self.toolbar.addAction(exitAction)
        # 设置窗口大小
        self.setGeometry(300, 300, 300, 200)
        # 设置窗口的标题
        self.setWindowTitle('Toolbar')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
