#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 14:31
# @Author  : zt

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


# 框布局 Boxlayout
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 设置按钮
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # 使用HBoxLayout和QVBoxLayout并添加伸展因子
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        # 设置窗口大小
        self.setGeometry(300, 300, 300, 150)
        # 设置窗口的标题
        self.setWindowTitle('Buttons')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
