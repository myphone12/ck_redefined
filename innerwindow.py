import tkinter as tk
from tkinter import ttk

class InnerWindow:

    def __init__(self,tk1,title:str = 'title'):
        self.tk = tk1
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.clicked = [0,0,0,0]
        self.move_states = ''
        self.move_start = [0,0]

        self.shadow = tk.Frame(self.tk,background='black')
        self.shadow.place(x=0,y=0,width=401,height=101)
        self.mainwindow = ttk.Frame(self.tk,relief='solid',borderwidth=1)
        self.mainwindow.place(x=0,y=0,width=400,height=100)
        self.innershadow = tk.Label(self.mainwindow,background='black')
        self.innershadow.place(x=2,y=2,width=396,height=96)
        self.titlebar = tk.Label(self.mainwindow,text=title,background='gray',anchor='w',relief='groove')
        self.titlebar.place(x=2,y=2,width=396,height=18)
        self.titlebar.bind('<ButtonPress-1>', self.on_drag_start)
        self.titlebar.bind('<B1-Motion>', self.on_drag_motion)
        self.titlebar.bind('<ButtonRelease-1>', self.on_drag_release)
        self.mainwindow.bind('<ButtonPress-1>', self.on_move_start)
        self.shadow.bind('<ButtonPress-1>', self.on_move_start)
        self.mainwindow.bind('<B1-Motion>', self.on_move_motion)
        self.shadow.bind('<B1-Motion>', self.on_move_motion)
        self.titlebutton1 = tk.Button(self.mainwindow,text='-',command=self.minimumwindow)
        self.titlebutton1.place(anchor='ne',x=339,y=2,width=30,height=18)
        self.titlebutton2 = tk.Button(self.mainwindow,text='□',command=self.maxwindow)
        self.titlebutton2.place(anchor='ne',x=369,y=2,width=30,height=18)
        self.titlebutton3 = tk.Button(self.mainwindow,text='X',command=self.closewindow)
        self.titlebutton3.place(anchor='ne',x=399,y=2,width=30,height=18)
    
    def windowplace(self,x,y):
        self.mainwindow.place_configure(x=x,y=y)
        self.shadow.place_configure(x=x+1,y=y+1)

    def windowmove(self,x,y):
        self.mainwindow.place_configure(width=x,height=y)
        self.shadow.place_configure(width=x+1,height=y+1)
        self.innershadow.place_configure(width=x-4,height=y-4)
        self.titlebar.place_configure(width=x-4)
        self.titlebutton1.place_configure(x=x-61)
        self.titlebutton2.place_configure(x=x-31)
        self.titlebutton3.place_configure(x=x-1)

    def on_drag_start(self,event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        self.clicked = [0,0,0,0]
        self.titlebutton2.configure(text='□')
 
    def on_drag_motion(self,event):
        p = self.mainwindow.place_info()
        x = int(p['x']) - self.drag_start_x + event.x
        y = int(p['y']) - self.drag_start_y + event.y
        self.windowplace(x,y)
 
    def on_drag_release(self,event):
        self.drag_start_x = 0
        self.drag_start_y = 0

    def on_move_start(self,event):
        self.move_start = [event.x,event.y]
        if event.x >= 4 and event.x <= int(self.mainwindow.place_info()['width']) - 4 and event.y >= int(self.mainwindow.place_info()['height']) - 4:
            self.move_states = 'down'
        elif event.x >= 4 and event.x <= int(self.mainwindow.place_info()['width']) - 4 and event.y <= 4:
            self.move_states = 'up'
        elif event.x <= 4 and event.y <=4:
            self.move_states = 'upleft'
        elif event.x <= 4 and event.y >= int(self.mainwindow.place_info()['height']) -4:
            self.move_states = 'downleft'
        elif event.x <= 2 and event.y >=2 and event.y <= int(self.mainwindow.place_info()['height']) :
            self.move_states = 'left'
        elif event.x >= int(self.mainwindow.place_info()['width']) - 4 and event.y <=4:
            self.move_states = 'upright'
        elif event.x >= int(self.mainwindow.place_info()['width']) - 4 and event.y >= int(self.mainwindow.place_info()['height']) -4:
            self.move_states = 'downright'
        elif event.x >= int(self.mainwindow.place_info()['width']) - 2 and event.y >=2 and event.y <= int(self.mainwindow.place_info()['height']) :
            self.move_states = 'right'
    
    def abs(self,num):
        if num < 0:
            return -num
        else:
            return num

    def on_move_motion(self,event):
        x = event.x
        y = event.y
        if self.move_states == 'up':
            self.windowmove(int(self.mainwindow.place_info()['width']),int(self.mainwindow.place_info()['height']) - self.move_start[1] - y)
            if int(self.mainwindow.place_info()['height'])>20:
                self.windowplace(int(self.mainwindow.place_info()['x']),int(self.mainwindow.place_info()['y']) + self.move_start[1] + y)
        if self.move_states == 'down':
            self.windowmove(int(self.mainwindow.place_info()['width']),y)
        if self.move_states[-5:-1] == 'righ':
            if self.move_states[0:2] == 'up':
                self.mainwindow.configure(cursor='pencil')
                self.windowmove(x,int(self.mainwindow.place_info()['height']) - self.move_start[1] - y)
                if int(self.mainwindow.place_info()['height'])>20:
                    self.windowplace(int(self.mainwindow.place_info()['x']),int(self.mainwindow.place_info()['y']) + self.move_start[1] + y)
            elif self.move_states[0:4] == 'down':
                self.windowmove(x,y)
            else:
                self.windowmove(x,int(self.mainwindow.place_info()['height']))
        if self.move_states[-4:-1] == 'lef':
            if self.move_states[0:2] == 'up':
                self.windowmove(int(self.mainwindow.place_info()['width']) - self.move_start[0] - x,int(self.mainwindow.place_info()['height']) - self.move_start[1] - y)
                if int(self.mainwindow.place_info()['height'])>20:
                    self.windowplace(int(self.mainwindow.place_info()['x']),int(self.mainwindow.place_info()['y']) + self.move_start[1] + y)
                if int(self.mainwindow.place_info()['width'])>92:
                    self.windowplace(int(self.mainwindow.place_info()['x']) + self.move_start[0] + x,int(self.mainwindow.place_info()['y']))
            elif self.move_states[0:4] == 'down':
                self.windowmove(int(self.mainwindow.place_info()['width']) - self.move_start[0] - x,y)
                if int(self.mainwindow.place_info()['width'])>92:
                    self.windowplace(int(self.mainwindow.place_info()['x']) + self.move_start[0] + x,int(self.mainwindow.place_info()['y']))
            else:
                self.windowmove(int(self.mainwindow.place_info()['width']) - self.move_start[0] - x,int(self.mainwindow.place_info()['height']))
                if int(self.mainwindow.place_info()['width'])>92:
                    self.windowplace(int(self.mainwindow.place_info()['x']) + self.move_start[0] + x,int(self.mainwindow.place_info()['y']))
        if int(self.mainwindow.place_info()['width'])<92:
            self.windowmove(92,int(self.mainwindow.place_info()['height']))
        if int(self.mainwindow.place_info()['height'])<=20:
            self.windowmove(int(self.mainwindow.place_info()['width']),20)
    def on_move_release(self,event):
        self.move_states = ''

    def maxwindow(self):
        if self.clicked == [0,0,0,0]:
            tmp = self.mainwindow.place_info()
            self.clicked = [int(tmp['x']),int(tmp['y']),int(tmp['width']),int(tmp['height'])]
            self.windowplace(0,0)
            self.windowmove(self.tk.winfo_width(),self.tk.winfo_height())
            self.titlebutton2.configure(text='▣')
        else:
            self.windowplace(self.clicked[0],self.clicked[1])
            self.windowmove(self.clicked[2],self.clicked[3])
            self.clicked = [0,0,0,0]
            self.titlebutton2.configure(text='□')

    def minimumwindow(self):
        self.windowplace(0,self.tk.winfo_height()-20)
        self.windowmove(92,20)
        self.self.clicked = [0,0,0,0]
        self.titlebutton2.configure(text='□')

    def closewindow(self):
        self.mainwindow.destroy()
        self.shadow.destroy()
        self.innershadow.destroy()
        self.titlebar.destroy()
        self.titlebutton1.destroy()
        self.titlebutton2.destroy()
        self.titlebutton3.destroy()