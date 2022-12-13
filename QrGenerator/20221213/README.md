# QRCode显示工具 version 20221213

## ini文件说明：

[Settings]
- pox：QRCode展示位置X轴，可选，默认为X轴最大值
- poy：QRCode展示位置Y轴，可选，默认为0
- imgsize：二维码尺寸
- separator：二维码信息分隔符
- exitflag：退出标志文件，当文件存在时退出二维码，可选
- scansec：扫描exitflag文件的间隔时间，秒
- imgname：保存的二维码图片文件名，可选

[BOMinfo]
- bompath：BOM路径
- uutidkey：测试机唯一标识符键名
- modelkey：MODEL键名
- panelkey：PANELTYPE信息来源
- jpkbkey：是否日本键盘的信息来源
- kbblkey：键盘背光信息来源（for PU1）
- kbbglval：键盘背光标识，KBPN倒数第三位（for PU2）
- gskuval：用来标识GSKU的字符串，以英文逗号间隔（for PU2）
- ylogopn：Y log灯标记来源（for PU1）
- rgbkb：RGB背光信息来源（for PU1）

[Output]
- values：按顺序列出需要显示的值，除modelkey和uutidkey为string外，其他为Y/N，以英文逗号间隔

## Notice：
- BOMinfo中不需要的信息，或者其他PU的信息可以用分号注释掉
- Output values的值，按顺序列出需要的部分即可