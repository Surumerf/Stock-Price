# coding: utf-8

'''
株価データのプロットとCSVへの出力
'''

import datetime as dt
import pandas as pd
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
    Vol = volume[::-1]
    Adj = adj_close[::-1]

    cdf = pd.DataFrame(index=Date)
    cdf["Open"] = Open
    cdf["High"] = High
    cdf["Low"] = Low
    cdf["Close"] = Close
    cdf["Volume"] = Vol
    cdf["Adj Close"] = Adj

    cdf.to_csv(code + '.csv')
    print(code + '.csvを出力しました．')

    print('株価データをプロット中．．．')
    df = pd.DataFrame(index=Date)
    df['Close'] = Adj

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
    df3 = pd.DataFrame(index=[])
    df3['Adj Close'] = df2['Adj Close']

    return df3

def main():
    country = str(input('日本株の場合は「ja」，そうでない場合は「us」を入力 [ja/us]: '))
    if country == 'ja':
        code = input('証券コード？ ')
        start_date = input('取得期間の初めの日付を入力 [yyyy-mm-dd]: ')
        end_date = input('取得期間の終わりの日付を入力 [yyyy-mm-dd]: ')
        try:
            jstock = jpstock(code, start_date, end_date)
            jstock['Close'].plot()
            plt.show()
        except:
            print('データの取得中にエラーが発生しました．')
            main()

    elif country == 'us':
        ticker = input('Ticker Symbol? :')
        start_date = input('取得期間の初めの日付を入力 [yyyy-mm-dd]: ')
        end_date = input('取得期間の終わりの日付を入力 [yyyy-mm-dd]: ')
        try:
            ustock = usstock(ticker, start_date, end_date)
            ustock['Adj Close'].plot()
            plt.show()
        except:
            print('データの取得中にエラーが発生しました．')
            main()

    else:
        print('エラーが発生しました．')
        main()

if __name__ == "__main__":
    main()
