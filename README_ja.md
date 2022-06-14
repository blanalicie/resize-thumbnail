# Resize Thumbnail

YoutubeとTwitter用にサムネイルをサイズ変換します。

----

## 事前準備

- opencv-python を実行環境にインストールしてください。
  - `ex.) pip install opencv-python`

----

## Usage

- resize_thumbnail.py を実行してください。引数には以下のようにサムネイルのファイルパスを渡します。
  - `ex.) python resize_thumbnail.py /path/to/source-thumbnail-image.png`

- 実行後、YoutubeとTwitter用のサムネイル画像が生成されます。
  - 出力先は元画像と同じディレクトリ内です。

----

## 動作環境

- Python 3.9.x が動けばなんでもいいと思います。たぶん。

----

## このスクリプトについて

- 1080pでサムネイルを作るとファイルサイズが2GBを超えてしまい、Youtubeで使用できないという事態が多々あります。
- でもせっかく1080pで作ったのに720pまで画質を落とすのは悲しいのです。
- なのでファイルサイズが2GBを超えない上限ギリギリぐらいのところまで画像を縮小するスクリプトを書きました。

