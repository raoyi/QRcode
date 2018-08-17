#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Runing with Python3
import os
import sys
import qrcode
from PIL import Image
import configparser

if len(sys.argv) == 1:
     if os.path.isfile('CreateQR.ini') == False:
          print("""
Configuration file not exist!
Or you can use parameter(s).

Usage:

     1. command mode
     
     CreateQR.py string-for-qr [qrsize:200] [mode:s(save)|w(show)|b(save&show)]
     
     2. configuration file mode
     
     need CreateQR.ini file and define content file in root path.
     
     CreateQR.ini format:
     
     [Config]
     logfile = content.txt
     imgsize = 200
     imgadd = QRcode.jpg
""")
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
          else:
               print("text file not exist!")
               sys.exit(2)
               
else:
     log = sys.argv[1]
     imgadd = "QRcode.jpg"
     if len(sys.argv) >= 3:
          if (sys.argv[2]).isdigit():
               imgsize = int(sys.argv[2])
          else:
               print("argv[2] should be digit.")
               sys.exit(3)
     else:
          imgsize = 200

#change size and output image
img = qrcode.make(''.join(log))
(x,y) = img.size
img = img.resize((imgsize,imgsize), Image.ANTIALIAS)

img.save(imgadd)

sys.exit(0)
