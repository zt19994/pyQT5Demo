#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 17:02
# @Author  : zt

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 创建了一个窗口
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit2.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        # 设置窗口大小
        self.setGeometry(300, 300, 350, 250)
        # 设置窗口的标题
        self.setWindowTitle('Main window')
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
