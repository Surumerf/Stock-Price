# 株価データのプロットとCSV出力

[![GitHub release](https://img.shields.io/github/release/Surumerf/Stock-Price.svg)](https://github.com/Surumerf/Stock-Price/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/Surumerf/Stock-Price.svg)](https://github.com/Surumerf/Stock-Price/commits)
[![Github commits (since latest release)](https://img.shields.io/github/commits-since/Surumerf/Stock-Price/latest.svg)](https://github.com/Surumerf/Stock-Price/commits)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/Surumerf/Stock-Price.svg)](https://github.com/Surumerf/Stock-Price)
[![license](https://img.shields.io/github/license/Surumerf/Stock-Price.svg)](LICENSE)

日本株または外国株の株価データを取得し，プロット・CSV出力を行います．

## インストール

実行するためには以下の環境とライブラリが必要です．

* Python 3.x
* matplotlib
* pandas
* pandas_datareader
* jsm

詳細は[こちら](https://qiita.com/Surumerf/items/436747326537143d1fcf)を参考にしてください．

## 使用方法

以下のコマンドで実行してください．

```batch
python stockprice-cli-v1.5.py
```

その後，日本株・外国株の選択や証券コード等の入力が求められます．  
指示に従って入力してください．

## ~~日本株データのCSV出力に関して~~

~~v1.0では日本株データを出力したCSVファイルにやや難があります．~~  
~~そのため出力されたCSVファイルを整形するファイル`modify.pl`を追加しました．~~  
~~CSVファイルと同じディレクトリに`modify.pl`を置いた上で，以下のコマンドで実行してください．~~

```batch
perl modify.pl < [旧CSVファイル名] > [新CSVファイル名]
```

v1.1で修正したため，`modify.pl`を削除しました．
