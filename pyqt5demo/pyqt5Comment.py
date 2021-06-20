#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 14:42
# @Author  : zt

import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)


# 评论回复布局demo
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # QLabel标签
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        # QLineEdit 单行文本编辑控件
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        # 表格布局
        grid = QGridLayout()
        # 表示各个控件之间的上下间距
        grid.setSpacing(10)
        # 设置表格中的位置 addWidget()方法用于向布局中添加控件
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        # 绑定布局
        self.setLayout(grid)
        # 设置窗口大小
        self.setGeometry(300, 300, 350, 300)
        # 设置窗口的标题
        self.setWindowTitle('Review')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
