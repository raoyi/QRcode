#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Runing with Python3
import os
import sys
import qrcode
from PIL import Image
import configparser

if os.path.isfile('CreateQR.ini') == False:
     print('Configuration file not exist!')
     sys.exit(1)
     
else:     
     conf = configparser.ConfigParser()
     conf.read('CreateQR.ini')
     logfile = conf.get('Config','logfile')
     imgsize = conf.getint('Config','imgsize')
     imgadd =  conf.get('Config','imgadd')
     
     #get QR message and generate image
     if os.path.isfile(logfile) == True:
          f = open(logfile)
          log = f.readlines(80)
          img = qrcode.make(''.join(log))
     else:
          print('Result file not exist, please check configuration file!')
          sys.exit(2)
    
#change size and output image
(x,y) = img.size
img = img.resize((imgsize,imgsize), Image.ANTIALIAS)
img.save(imgadd)
sys.exit(0)
