# カスタマーバーコード画像作成

カスバー画像を生成します。
※ Pillowを使用しています

## 概要

日本郵政が公開してる下記ツールのカスバー生成ロジックをベースに作成。

https://www.post.japanpost.jp/useful_tool/barcode/index.html

戻りで画像とバーコード文字列のリスト（スタート／ストップコードを除く）を返却。

※ 郵便局への持ち込みで読取テスト等はまだ行っていません ※

住所の文字列からバーコード用データ抽出するモジュール追加
コード抽出は下記サイトの検証データはクリアしてます。

https://www.post.japanpost.jp/zipcode/zipmanual/p25.html


性能的には

カスバー用のコード抽出：0.1ms / 件
カスバー画像作成：0.6ms / 件

画像の保存までやると1件：1.5ms程度




## 使用例

```
import gencbar

gcbar = gencbar.GenCBar()
barstr = "10000131-3-2-503"
img, barcode = gcbar.create_bar(barstr)
img.save("customer_barcode.png")
print(barcode)

cbardata = gencbar.Addr2CBarData()
yuubin = '2630023'
addr = '千葉市稲毛区緑町3丁目30-8　郵便ビル403号'
barstr = cbardata.get_ccode_all(yuubin,addr)

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
pip install dist/GenCBar-0.2.tar.gz
#その内PyPIに上げる
```




