#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 11:33
# @Author  : zt

import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication


# 绝对定位
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    # 使用move()方法来控制控件的位置
    def init_ui(self):
        # QLabel 设置label
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)
        # 设置窗口大小
        self.setGeometry(300, 300, 250, 150)
        # 设置窗口的标题
        self.setWindowTitle('Absolute')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
