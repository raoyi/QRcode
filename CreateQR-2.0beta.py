#!/usr/bin/env python
#Python3 supported

import os
import sys
import tkinter
import qrcode
from PIL import Image, ImageTk
import configparser

if len(sys.argv) == 1:
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
          else:
               print('Result file not exist, please check configuration file!')
               sys.exit(2)

else:
     log = sys.argv[1]
     imgsize = 500
     if len(sys.argv) >= 3 and type(sys.argv[2])==int:
          imgsize =sys.argv[2]
          
#change size and output image
img = qrcode.make(''.join(log))
(x,y) = img.size
img = img.resize((imgsize,imgsize), Image.ANTIALIAS)

#create window
uisize = str(imgsize) + "x" + str(imgsize)
uidef = uisize + "+10+10"
imgpos = imgsize/2

root = tkinter.Tk()
#set window top
root.wm_attributes('-topmost',1)
#hide the title bar
root.overrideredirect(True)

#root.attributes("-alpha", 0.4)

root.geometry(uidef)
canvas = tkinter.Canvas(root)
uibg = ImageTk.PhotoImage(img)
canvas.create_image(imgpos,imgpos,image = uibg)
canvas.configure(highlightthickness = 0)
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

sys.exit(0)
