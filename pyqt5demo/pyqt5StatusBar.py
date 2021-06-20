#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 16:35
# @Author  : zt

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


# 状态栏
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # statusBar 状态栏
        self.statusBar().showMessage('Ready')
        # 设置窗口大小
        self.setGeometry(300, 300, 250, 150)
        # 设置窗口的标题
        self.setWindowTitle('Statusbar')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
