#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python2.7 support

import os
import sys
import Tkinter
import ImageTk
import qrcode
import Image
import ConfigParser

if len(sys.argv) == 1:
     if os.path.isfile('CreateQR.ini') == False:
          print('Configuration file not exist!')
          sys.exit(1)

     else:
          conf = ConfigParser.ConfigParser()
          conf.read('CreateQR.ini')
          logfile = conf.get('Config','logfile')
          imgsize = conf.getint('Config','imgsize')
          imgadd =  conf.get('Config','imgadd')

          #get QR message and generate image
          if os.path.isfile(logfile) == True:
               f = open(logfile)
               log = f.readlines(80)
          else:
               print('Result file not exist, please check configuration file!')
               sys.exit(2)

else:
     log = sys.argv[1]
     imgsize = 200
     if len(sys.argv) >= 3:
          imgsize = int(sys.argv[2])
          
#change size and output image
img = qrcode.make(''.join(log))
(x,y) = img.size
img = img.resize((imgsize,imgsize), Image.ANTIALIAS)

#create window
uisize = str(imgsize)+"x"+str(imgsize)

root = Tkinter.Tk()
#set window top
root.wm_attributes('-topmost',1)
#hide the title bar
root.overrideredirect(True)

imglb = ImageTk.PhotoImage(img)
Tkinter.Label(root, image=imglb).pack(side="top")

root.geometry(uisize+"+10+10")

root.mainloop()

sys.exit(0)
