#!usr/bin/python3
# -*- coding:utf-8 -*-

'''
株価データのプロット・CSVの出力 (GUI Version)
'''

'''
[v1.5 Alpha 1] GUIのみ実装，データ取得機能は未実装
'''

import sys
'''
import datetime as dt
from pandas import DataFrame
import jsm
import pandas_datareader as web
import matplotlib.pyplot as plt
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont

class Tab1Widget(QMainWindow):
    def __init__(self, parent=None):
        super(Tab1Widget, self).__init__()
        self.label = QLabel('証券コード', self)
        self.font = QFont('Yu Gothic UI', 11)
        self.label.setFont(self.font)
        self.label.move(20, 20)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 60)
        self.textbox.resize(280, 40)

        self.button = QPushButton('取得', self)
        self.button.move(320, 70)
        self.button.clicked.connect(self.on_click)

        self.label2 = QLabel('業種別銘柄リスト', self)
        self.label2.setFont(self.font)
        self.label2.move(20, 140)
        self.label2.resize(200, 30)

        combo = QComboBox(self)
        lists = [
            'a',
            'b',
            'c'
        ]
        combo.addItems(lists)
        combo.move(20, 180)
        combo.activated[str].connect(self.onActivated)

    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message', 'You typed: ' + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    def onActivated(self, text):
        QMessageBox.question(self, 'Message', 'You chosed: ' + text, QMessageBox.Ok, QMessageBox.Ok)

class Tab2Widget(QMainWindow):
    def __init__(self, parent=None):
        super(Tab2Widget, self).__init__()
        self.label = QLabel('Ticker Symbol', self)
        self.font = QFont('Yu Gothic UI', 11)
        self.label.setFont(self.font)
        self.label.move(20, 20)
        self.label.resize(200, 30)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 60)
        self.textbox.resize(280, 40)
        self.button = QPushButton('取得', self)
        self.button.move(320, 70)

class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        qtab = QTabWidget()
        qtab.addTab(Tab1Widget(parent=self), '日本株')
        qtab.addTab(Tab2Widget(parent=self), '外国株')

        hbox = QHBoxLayout()
        hbox.addWidget(qtab)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Stock Price')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())
