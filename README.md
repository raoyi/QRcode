# QRcode [![LICENSE](https://img.shields.io/github/license/raoyi/qrcode.svg)](https://github.com/raoyi/QRcode/blob/master/LICENSE)

Create and display QR code according to the text

`CreateQR.py —— Create QRcode`

`content.txt —— QR code data source`

`CreateQR.ini —— configuration file`

`showQR.au3 —— run exe file, show the code image`

1.0版本，依据配置文件生成二维码图片

1.1版本，不再需要au3文件，并且支持命令行（可以不需要ini文件和txt文件）。但暂时不能定时刷新，待更新。

2.0beta版本，支持鼠标拖动。但图片尺寸设置有问题，需要修正。

2.0版本目标：

1. 同时支持命令行和配置文件模式（已完成）

2. 可自由选择保存图片、显示图片或保存并显示图片（已完成）

3. 显示图片时支持鼠标拖动窗口（已完成）

注意：已经存在同名图片时，会删除旧文件
