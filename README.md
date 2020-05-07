# image-organizer

pathlib の練習用

## Overview

画像整理スクリプト

## Description

画像ファイル、動画ファイルの作成日時を元にフォルダを作成、リネームを行いすっきり整理

## Demo

## Requirement

## Usage

before

```
/hoge
|--asdf (1).JPG
|--asdf (1).mp4
|--asdf (2).JPG
|--asdf (3).JPG
|--asdf (4).JPG
```

Execute

```
python organize-image.py hoge
Move to: temp/hoge/IMG/2019-10-29/IMG_20191029_123338.JPG
Move to: temp/hoge/VID/2019-10-23/VID_20191023_072248.mp4
Move to: temp/hoge/IMG/2019-10-29/IMG_20191029_201141.JPG
Move to: temp/hoge/IMG/2019-10-29/IMG_20191029_204542.JPG
Move to: temp/hoge/IMG/2019-10-29/IMG_20191029_225213.JPG
```

after

```
hoge
|--IMG
|  |--2019-10-29
|  |  |--IMG_20191029_123338.JPG
|  |  |--IMG_20191029_201141.JPG
|  |  |--IMG_20191029_204542.JPG
|  |  |--IMG_20191029_225213.JPG
|--VID
|  |--2019-10-23
|  |  |--VID_20191023_072248.mp4
```

## Install

## Contribution

## Licence

## Author

[okojomoeko](https://github.com/okojomoeko)
