#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: skip-file

'''
Plotting and CSV-Exporting Stock Prices Data (CLI Version)
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

    print('Exporting CSV Files . . .')
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
    print(code + '.csv exported.')

    print('Plotting . . .')
    df = DataFrame(index=Date)
    df['Adj Close'] = Adj

    return df

def usstock(ticker, start_date, end_date):
    year, month, day = start_date.split("-")
    start = dt.date(int(year), int(month), int(day))
    year, month, day = end_date.split("-")
    end = dt.date(int(year), int(month), int(day))

    print('Exporting CSV Files . . .')
    df2 = web.DataReader(ticker, 'yahoo', start, end)

    df2.to_csv(ticker + '.csv')
    print(ticker + '.csv exported.')

    print('Plotting . . .')
    df3 = DataFrame(index=[])
    df3['Adj Close'] = df2['Adj Close']

    return df3

def brand():
    print('Displaying the list of Industry Code . . .')

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

    gcode = input('Industries Code? ')
    print('Displaying the list of names classified into the designated industry . . .')
    q = jsm.Quotes()
    brands = q.get_brand(gcode)
    bf4 = DataFrame()
    bf4["List of Names"] = brands
    print(bf4)
    print('Exporting the list . . .')
    bf4.to_csv(gcode + '.txt', index=False)
    print(gcode + '.txt exported.')

    cont = str(input('Continue(y) or Exit(n)? [y/n]: '))
    if cont == 'n':
        return None
    else:
        main()


def main():
    country = str(input('Japanese Stocks(ja) or Non-Japanese(us)? [ja/us]: '))
    if country == 'ja':
        code = input('Securities Code? ')
        if str(code) == "search":
            try:
                brand()
            except:
                print('Error occured while retrieving data.')
                main()
        else:
            start_date = input('From when? [yyyy-mm-dd]: ')
            end_date = input('Until when? [yyyy-mm-dd]: ')
            try:
                jstock = jpstock(code, start_date, end_date)
                jstock['Adj Close'].plot()
                plt.show()
                main()
            except:
                print('Error occured while retrieving data.')
                main()

    elif country == 'us':
        ticker = input('Ticker Symbol?: ')
        start_date = input('From when? [yyyy-mm-dd]: ')
        end_date = input('Until when? [yyyy-mm-dd]: ')
        try:
            ustock = usstock(ticker, start_date, end_date)
            ustock['Adj Close'].plot()
            plt.show()
            main()
        except:
            print('Error occured while retrieving data.')
            main()

    elif country == 'exit':
        return

    else:
        print('Enter [ja] or [us]')
        main()

if __name__ == "__main__":
    main()
