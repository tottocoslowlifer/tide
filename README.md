# 「潮位予測からのアクティビティの選定」リポジトリ
このリポジトリの説明.
2024年2月から.

## 概要

## フォルダの説明
### data
使うデータを置くフォルダ.

### notebooks
分析に使うipynbファイルを置くフォルダ.

### scripts
実行プログラムであるPythonファイルを置くフォルダ.

## 実行方法
1. `scripts`ディレクトリに移動する.
2. `data/Moji_Tide_2011-2021/raw`内の各ファイルを保存する.
3. 次のコマンドを入力し, 実行完了まで待つ.
  ~~~
  python3 csv_convert.py
  ~~~
4. `data/Moon_2011-2021/raw`内の各ファイル`mooncal20xx.csv`を保存する.
5. 次のコマンドを入力し, 実行完了まで待つ.
  ~~~
  python3 Moon_convert.py
  ~~~
6. `data/Shimonoseki_2011-2021`内の各フォルダに対し,`raw`内の各ファイルを保存する.
7. 次のコマンドを入力し, 実行完了まで待つ.
  ~~~
  python3 Shimonoseki_integrate.py
  ~~~