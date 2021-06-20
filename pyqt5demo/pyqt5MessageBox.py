#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 22:22
# @Author  : zt

import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUI方法
        self.init_ui()

    def init_ui(self):
        # 设置窗口大小
        self.setGeometry(300, 300, 250, 150)
        # 设置窗口的标题
        self.setWindowTitle('Message box')
        # 显示窗口
        self.show()

    def closeEvent(self, event):
        # 关闭窗口的时候,触发了QCloseEvent。我们需要重写closeEvent()事件处理程序。
        # 我们显示一个消息框,两个按钮:“是”和“不是”。
        # 第一个字符串出现在titleBar。
        # 第二个字符串消息对话框中显示的文本。
        # 第三个参数指定按钮的组合出现在对话框中。
        # 最后一个参数是默认按钮，这个是默认的按钮焦点。
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
