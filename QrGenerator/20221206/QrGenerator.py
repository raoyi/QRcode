#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import qrcode
import tkinter, tkinter.messagebox
from PIL import Image, ImageTk
import configparser
import threading
import time

# get filename
name = os.path.split(__file__)[-1]
name = name[:name.rfind('.')]

# del log
if os.path.exists(name+'log.txt'):
    os.remove(name+'log.txt')

settings = ['pox','poy','imgsize','separator','exitflag','scansec','imgname']
for i in settings:
    globals()[i] = ''

config = configparser.ConfigParser()
config.read(name+'.ini',encoding='utf-8')

# variables assignment
globals().update(dict(config._sections['Settings']))
globals().update(dict(config._sections['BOMinfo']))
globals().update(dict(config._sections['Output']))

def error(msg):
    root = tkinter.Tk()
    root.withdraw() # hide main window
    tkinter.messagebox.showerror('ERROR',msg)
    os._exit(0)
    
valist = values.split(',')

try:
    imgsize = int(imgsize)
except ValueError:
    error('imgsize in INI file must be int!')
else:
    pass

try:
    scansec = int(scansec)
except ValueError:
    error('scansec in INI file must be int!')
else:
    pass

if exitflag == '':
    error('exit flag not exist!')

# 创建字典存储查询结果
replace_dict = {}
if 'ylogopn' in valist:
    replace_dict['ylogopn'] = 'N'
if 'rgbkb' in valist:
    replace_dict['rgbkb'] = 'N'

# check BOM
if os.path.exists(bompath):
    with open(bompath,'r',encoding='utf-8') as file:
        # 判断是否为GSKU
        if 'gskuval' in valist:
            if file.read().find(gskuval) == -1:
                replace_dict['gskuval'] = 'N'
            else:
                replace_dict['gskuval'] = 'Y'

        file.seek(0)
        for line in file.readlines():
            # 获取PF号，字符串
            if 'uutidkey' in valist:
                if uutidkey+'=' in line:
                    replace_dict['uutidkey'] = line.split('=')[1].replace('\n','').strip()

            # 获取机型，字符串
            if 'modelkey' in valist:
                if modelkey+'=' in line:
                    replace_dict['modelkey'] = line.split('=')[1].replace('\n','').strip()

            # 判断是否有指纹，若为N/A->N，否则为Y
            if 'fpkey' in valist:
                if fpkey+'=' in line:
                    fp = line.split('=')[1].replace('\n','').strip()
                    if fp == 'N/A':
                        replace_dict['fpkey'] = 'N'
                    else:
                        replace_dict['fpkey'] = 'Y'

            # 判断是否触摸屏，若为N/A->N，否则为Y
            if 'panelkey' in valist:
                if panelkey+'=' in line:
                    panel = line.split('=')[1].replace('\n','').strip()
                    if panel == 'N/A':
                        replace_dict['panelkey'] = 'N'
                    else:
                        replace_dict['panelkey'] = 'Y'

            #判断键盘背光，若为BL->Y，否则为N。番外：若值为BL，为白背光
            if 'kbblkey' in valist:
                if kbblkey+'=' in line:
                    kbbl = line.split('=')[1].replace('\n','').strip()
                    if kbbl == 'BL':
                        replace_dict['kbblkey'] = 'Y'
                    else:
                        replace_dict['kbblkey'] = 'N'

            # 判断是否存在A壳Y灯
            if 'ylogopn' in valist:
                if 'MTNAMEPN=' in line:
                    mtnpn = line.split('=')[1].replace('\n','').strip()
                    mtnlist = ylogopn.split(',')
                    if mtnpn in mtnlist:
                        replace_dict['ylogopn'] = 'Y'

            # RGB背光
            if 'rgbkb' in valist:
                colkblist = rgbkb.split(',')
                if 'KBSPEC2'==colkblist[0]:
                    if 'KBSPEC2=' in line:
                        kbspc = line.split('=')[1].replace('\n','').strip()
                        if kbspc == 'RGB BL':
                            replace_dict['rgbkb'] = 'Y'
                elif 'KBSPEC4'==colkblist[0]:
                    if 'KBSPEC4=' in line:
                        kbspc = line.split('=')[1].replace('\n','').strip()
                        if kbspc == 'RGB':
                            replace_dict['rgbkb'] = 'Y'
                elif 'KBPN=' in line:
                    colkb = line.split('=')[1].replace('\n','').strip()
                    if colkb in colkblist:
                        replace_dict['rgbkb'] = 'Y'

    file.close()
else:
    error('BOM.BAT NOT EXIST or BOMPATH ERROR!')

#print(replace_dict)
res_list = [replace_dict[i] if i in replace_dict else i for i in valist]

strings = separator.join(res_list)
#print(strings)

# set QR
qr = qrcode.QRCode(
    #version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    #box_size=10,
    border=1,
)

# create QR, change size and output image
qr.add_data(strings)
qr.make(fit=True)
img = qr.make_image()
img = img.resize((imgsize,imgsize))

if imgname != '':
    img.save(imgname)

# create window
uisize = str(imgsize)+"x"+str(imgsize)

root = tkinter.Tk()
# set window top
root.wm_attributes('-topmost',1)
# hide the title bar
root.overrideredirect(True)

imglb = ImageTk.PhotoImage(img)
tkinter.Label(root, image=imglb).pack(side="top")

if pox == '':
    pox = str(root.winfo_screenwidth()-imgsize)
if poy == '':
    poy = str(0)
    
root.geometry(uisize+"+"+pox+"+"+poy)

def autoExit():
    #time.sleep(1)
    while not os.path.exists(exitflag):
        #print('delay secs...')
        time.sleep(scansec)
    f = open(name+'log.txt', 'w+')
    f.write('Show QRCode PASS')
    f.close()
    root.destroy()

t = threading.Thread(target=autoExit)
t.start()
root.bind_all("<Escape>", lambda event: root.destroy())
root.mainloop()
os._exit(0)
