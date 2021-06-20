#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 21:35
# @Author  : zt

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 这种静态的方法设置一个用于显示工具提示的字体，我们使用10px滑体字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个提示，我们称之为setToolTip方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建一个PushButton并为它设置一个toolTip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 设置btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        # 移动窗口的位置
        btn.move(50, 50)

        # 设置窗口大小
        self.setGeometry(300, 300, 300, 200)
        # 设置窗口的标题
        self.setWindowTitle("ToolTip")
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
