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
1. 以下のコマンドを入力する.
~~~
echo 'export PYTHONPATH=../..' >> ~/.bashrc
~~~
~~~
source ~/.bashrc
~~~
~~~
pip3 install --upgrade pip
~~~
~~~
pip3 install -r requirements.txt
~~~

2. `scripts/make_data`ディレクトリ上で,次のコマンドを順に入力する.
  ~~~
  python3 csv_convert.py
  ~~~
  ~~~
  python3 Moon_convert.py
  ~~~
  ~~~
  python3 Shimonoseki_integrate.py
  ~~~
  ~~~
  python3 preprocessed_csv_convert.py
  ~~~

3. `scripts/try`ディレクトリ上で,次のコマンドを入力する.
~~~
python3 test.py
~~~
