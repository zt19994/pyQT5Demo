#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 21:20
# @Author  : zt

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


# 设置icon
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 设置窗口大小
        self.setGeometry(300, 300, 300, 300)
        # 设置窗口的标题
        self.setWindowTitle("Icon")
        # 设置窗口图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.png'))
        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
