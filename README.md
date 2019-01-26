# カスタマーバーコード画像作成

カスバー画像を生成します。
※ Pillowを使用しています

## 概要

日本郵政が公開してる下記ツールのカスバー生成ロジックをベースに作成。

https://www.post.japanpost.jp/useful_tool/barcode/index.html

戻りで画像とバーコード文字列のリスト（スタート／ストップコードを除く）を返却。

## 使用例

```
import gencbar

gcbar = gencbar.GenCBar()
barstr = "10000131-3-2-503"
img, barcode = gcbar.create_bar(barstr)
img.save("customer_barcode.png")
print(barcode)
```


## テスト

```
pytest test.py
```


## ビルド

```
python setup.py sdist
```



## インストール

```
pip install dist/GenCBar-0.1.tar.gz
#その内PyPIに上げる
```




