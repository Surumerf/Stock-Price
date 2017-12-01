#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
株価データのプロット・CSVへの出力
'''

import datetime as dt
from pandas import DataFrame
import jsm
import pandas_datareader.data as web
import matplotlib.pyplot as plt

def jpstock(code, start_date, end_date):
    year, month, day = start_date.split("-")
    start = dt.date(int(year), int(month), int(day))
    year, month, day = end_date.split("-")
    end = dt.date(int(year), int(month), int(day))

    print('CSVを出力中．．．')
    q = jsm.Quotes()
    target = q.get_historical_prices(code, jsm.DAILY, start_date=start, end_date=end)

    date = [data.date for data in target]
    open = [data.open for data in target]
    high = [data.high for data in target]
    low = [data.low for data in target]
    close = [data.close for data in target]
    volume = [data.volume for data in target]
    adj_close = [data._adj_close for data in target]

    Date = date[::-1]
    Open = open[::-1]
    High = high[::-1]
    Low = low[::-1]
    Close = close[::-1]
    Adj = adj_close[::-1]
    Vol = volume[::-1]

    cdf = DataFrame(index=Date)
    cdf.index.name = "Date"
    cdf["Open"] = Open
    cdf["High"] = High
    cdf["Low"] = Low
    cdf["Close"] = Close
    cdf["Adj Close"] = Adj
    cdf["Volume"] = Vol

    cdf.to_csv(code + '.csv')
    print(code + '.csvを出力しました．')

    print('株価データをプロット中．．．')
    df = DataFrame(index=Date)
    df['Adj Close'] = Adj

    return df

def usstock(ticker, start_date, end_date):
    year, month, day = start_date.split("-")
    start = dt.date(int(year), int(month), int(day))
    year, month, day = end_date.split("-")
    end = dt.date(int(year), int(month), int(day))

    print('CSVを出力中．．．')
    df2 = web.DataReader(ticker, 'yahoo', start, end)

    df2.to_csv(ticker + '.csv')
    print(ticker + '.csvを出力しました．')

    print('株価データをプロット中．．．')
    df3 = DataFrame(index=[])
    df3['Adj Close'] = df2['Adj Close']

    return df3

def brand():
    print('業種コード一覧を表示します．．．')

    lists = [ 
        "'0050': 農林・水産業",
        "'1050': 鉱業",
        "'2050': 建設業",
        "'3050': 食料品",
        "'3100': 繊維製品",
        "'3150': パルプ・紙",
        "'3200': 化学",
        "'3250': 医薬品",
        "'3300': 石油・石炭製品",
        "'3350': ゴム製品",
        "'3400': ガラス・土石製品",
        "'3450': 鉄鋼",
        "'3500': 非鉄金属",
        "'3550': 金属製品",
        "'3600': 機械",
        "'3650': 電気機器",
        "'3700': 輸送機器",
        "'3750': 精密機器",
        "'3800': その他製品",
        "'4050': 電気・ガス業",
        "'5050': 陸運業",
        "'5100': 海運業",
        "'5150': 空運業",
        "'5200': 倉庫・運輸関連業",
        "'5250': 情報・通信",
        "'6050': 卸売業",
        "'6100': 小売業",
        "'7050': 銀行業",
        "'7100': 証券業",
        "'7150': 保険業",
        "'7200': その他金融業",
        "'8050': 不動産業",
        "'9050': サービス業"
    ]

    for item in lists:
        print(item)

    gcode = input('業種コード？ ')
    print('業種別銘柄リストを取得しています．．．')
    q = jsm.Quotes()
    brands = q.get_brand(gcode)
    bf4 = DataFrame()
    bf4["銘柄リスト"] = brands
    print(bf4)
    print('リストファイルを出力中．．．')
    bf4.to_csv(gcode + '.txt', index=False)
    print(gcode + '.txtを出力しました．')

    cont = str(input('引き続き個別銘柄のデータを取得する場合は「y」，やめる場合は「n」を入力 [y/n]: '))
    if cont == 'n':
        return None
    else:
        main()


def main():
    country = str(input('日本株の場合は「ja」，そうでない場合は「us」を入力 [ja/us]: '))
    if country == 'ja':
        code = input('証券コード？ ')
        if str(code) == "search":
            try:
                brand()
            except:
                print('データの取得中にエラーが発生しました．')
                main()
        else:
            start_date = input('取得期間の初めの日付を入力 [yyyy-mm-dd]: ')
            end_date = input('取得期間の終わりの日付を入力 [yyyy-mm-dd]: ')
            try:
                jstock = jpstock(code, start_date, end_date)
                jstock['Adj Close'].plot()
                plt.show()
            except:
                print('データの取得中にエラーが発生しました．')
                main()

    elif country == 'us':
        ticker = input('Ticker Symbol?: ')
        start_date = input('取得期間の初めの日付を入力 [yyyy-mm-dd]: ')
        end_date = input('取得期間の終わりの日付を入力 [yyyy-mm-dd]: ')
        try:
            ustock = usstock(ticker, start_date, end_date)
            ustock['Adj Close'].plot()
            plt.show()
        except:
            print('データの取得中にエラーが発生しました．')
            main()

    elif country == 'exit':
        return

    else:
        print('[ja/us] を入力してください．')
        main()

if __name__ == "__main__":
    main()
