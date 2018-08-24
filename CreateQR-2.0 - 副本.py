#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Runing with Python3
import os
import sys
import qrcode
import tkinter
from PIL import Image, ImageTk
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
          elif sys.argv[2] == '':
               imgsize = 200
          else:
               print("argv[2] should be digit.")
               sys.exit(3)
     else:
          imgsize = 200

#change size and output image
img = qrcode.make(''.join(log))
(x,y) = img.size
img = img.resize((imgsize,imgsize), Image.ANTIALIAS)


if len(sys.argv) >= 4:
     if sys.argv[3] == 'w' or sys.argv[3] == 'b':
          if sys.argv[3] == 'b':
               img.save(imgadd)
               
          #create window
          uisize = str(imgsize) + "x" + str(imgsize)
          uidef = uisize + "+10+10"
          imgpos = imgsize/2

          root = tkinter.Tk()
          #set window top
          root.wm_attributes('-topmost',1)
          #hide the title bar
          root.overrideredirect(True)
          root.geometry(uidef)
          canvas = tkinter.Canvas(root,width=imgsize,height=imgsize,bd=0,highlightthickness=0)
          uibg = ImageTk.PhotoImage(img)
          canvas.create_image(imgpos,imgpos,image = uibg)
          canvas.pack()
          x, y = 0, 0

          def move(event):
               global x,y
               new_x = (event.x-x)+root.winfo_x()
               new_y = (event.y-y)+root.winfo_y()
               s = uisize + "+" + str(new_x)+"+" + str(new_y)
               root.geometry(s)

          def button_1(event):
               global x,y
               x,y = event.x,event.y

          canvas.bind("<B1-Motion>",move)
          canvas.bind("<Button-1>",button_1)
          root.mainloop()
     else:
          img.save(imgadd)
else:
     img.save(imgadd)

sys.exit(0)
