#!usr/bin/python3
# -*- coding:utf-8 -*-

'''
株価データのCSV出力 (GUI Version)
'''

'''
[v1.5 Alpha 2] 期間設定機能・プロット機能は未実装
'''

import sys
import datetime as dt
from pandas import DataFrame
import jsm
import pandas_datareader as web
import matplotlib.pyplot as plt
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

        self.combo = QComboBox(self)
        lists = [
            "",
            "0050 : 農林・水産業",
            "1050 : 鉱業",
            "2050 : 建設業",
            "3050 : 食料品",
            "3100 : 繊維製品",
            "3150 : パルプ・紙",
            "3200 : 化学",
            "3250 : 医薬品",
            "3300 : 石油・石炭製品",
            "3350 : ゴム製品",
            "3400 : ガラス・土石製品",
            "3450 : 鉄鋼",
            "3500 : 非鉄金属",
            "3550 : 金属製品",
            "3600 : 機械",
            "3650 : 電気機器",
            "3700 : 輸送機器",
            "3750 : 精密機器",
            "3800 : その他製品",
            "4050 : 電気・ガス業",
            "5050 : 陸運業",
            "5100 : 海運業",
            "5150 : 空運業",
            "5200 : 倉庫・運輸関連業",
            "5250 : 情報・通信",
            "6050 : 卸売業",
            "6100 : 小売業",
            "7050 : 銀行業",
            "7100 : 証券業",
            "7150 : 保険業",
            "7200 : その他金融業",
            "8050 : 不動産業",
            "9050 : サービス業"
        ]
        self.combo.addItems(lists)
        self.combo.move(20, 180)
        self.combo.resize(200, 30)

        self.button2 = QPushButton('取得', self)
        self.button2.move(240, 180)
        self.button2.clicked.connect(self.on_click2)

    def on_click(self):
        code = int(self.textbox.text())
        self.start = dt.date(2017, 10, 1)
        self.end = dt.date(2017, 10, 31)

        q = jsm.Quotes()
        target = q.get_historical_prices(code, jsm.DAILY, start_date=self.start, end_date=self.end)

        self.date = [data.date for data in target]
        self.open = [data.open for data in target]
        self.high = [data.high for data in target]
        self.low = [data.low for data in target]
        self.close = [data.close for data in target]
        self.volume = [data.volume for data in target]
        self.adj_close = [data._adj_close for data in target]

        self.Date = self.date[::-1]
        self.Open = self.open[::-1]
        self.High = self.high[::-1]
        self.Low = self.low[::-1]
        self.Close = self.close[::-1]
        self.Adj = self.adj_close[::-1]
        self.Vol = self.volume[::-1]

        cdf = DataFrame(index=self.Date)
        cdf.index.name = "Date"
        cdf["Open"] = self.Open
        cdf["High"] = self.High
        cdf["Low"] = self.Low
        cdf["Close"] = self.Close
        cdf["Adj Close"] = self.Adj
        cdf["Volume"] = self.Vol

        cdf.to_csv(str(code) + '.csv')

        QMessageBox.question(self, 'Exported CSV', str(code) + '.csv を出力しました．', QMessageBox.Ok, QMessageBox.Ok)

        self.textbox.setText("")

    def on_click2(self):
        gcode = int(self.combo.currentIndex())
        
        if gcode > 0:
            brandlist = [
                "0050",
                "1050",
                "2050",
                "3050",
                "3100",
                "3150",
                "3200",
                "3250",
                "3300",
                "3350",
                "3400",
                "3450",
                "3500",
                "3550",
                "3600",
                "3650",
                "3700",
                "3750",
                "3800",
                "4050",
                "5050",
                "5100",
                "5150",
                "5200",
                "5250",
                "6050",
                "6100",
                "7050",
                "7100",
                "7150",
                "7200",
                "8050",
                "9050"
            ]
            q = jsm.Quotes()
            brands = q.get_brand(brandlist[gcode-1])
            df = DataFrame()
            df["銘柄リスト"] = brands
            df.to_csv(brandlist[gcode-1] + '.txt', index=False)
            QMessageBox.question(self, 'Exported list', brandlist[gcode-1] + '.txt を出力しました．', QMessageBox.Ok, QMessageBox.Ok)
            
            self.combo.setCurrentIndex(0)

        else:
            self.combo.setCurrentIndex(0)

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
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        ticker = self.textbox.text()
        self.start = dt.date(2017, 10, 1)
        self.end = dt.date(2017, 10, 31)

        df = web.DataReader(ticker, 'yahoo', self.start, self.end)
        df.to_csv(str(ticker) + '.csv')

        QMessageBox.question(self, 'Exported CSV', str(ticker) + '.csv を出力しました．', QMessageBox.Ok, QMessageBox.Ok)

        self.textbox.setText("")

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
