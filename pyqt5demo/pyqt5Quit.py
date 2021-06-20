#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 21:58
# @Author  : zt

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


# 退出窗口
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 创建一个PushButton
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 设置btn.sizeHint()显示默认尺寸
        qbtn.resize(qbtn.sizeHint())
        # 移动窗口的位置
        qbtn.move(50, 50)

        # 设置窗口大小
        self.setGeometry(300, 300, 250, 150)
        # 设置窗口的标题
        self.setWindowTitle('Quit button')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
