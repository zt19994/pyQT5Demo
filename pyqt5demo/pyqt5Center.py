#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 22:27
# @Author  : zt

import sys

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # resize()方法调整窗口大小，这里是250px宽150px高
        self.resize(250, 150)
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('Center')
        # 显示窗口
        self.show()

    # 控制窗口显示在屏幕中心的方法
    # QtGui.QDesktopWidget类提供了用户的桌面信息,包括屏幕大小。
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
