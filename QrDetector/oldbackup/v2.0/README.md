# 二维码识别 - version2.0

设置多个值，当扫到设定值之一时，退出，并把结果存到txt文档

若扫到二维码的值不包含在设定值中（全字符串匹配），则不做任何动作，持续扫码

ini文件设置：
- setchar：列出所需字符串的所有可能性，以separator的值分隔
- separator：与setchar的值配合，用于分隔各种可能性
- debug：当debug=Y时，每次扫到不同的码会截图并保存，图片以时间戳命名