import wave,pydub,threading
import pydub.effects
from pydub.playback import play
import tkinter as tk
from tkinter import ttk , messagebox as msg
from UI import _UI

# class inner
class Sound(_UI):

    def __init__(self):
        super().__init__()
        self.textvar = tk.StringVar()
        self.audio = [pydub.AudioSegment.from_wav(i) for i in ['5.wav','鹅.wav','啊.wav','鹅2.wav','er.wav']]
        self.sound = [0,0,0,0,0]
        self.playline = False
        self.now = [0,0,0,0]
        self.audionamelist = ('5','鹅','啊','鹅','er')
        self.length = -1
    
    def Playsound(self,data):
        self.thread = threading.Thread(target=lambda:self._Playsound(data))
        self.thread.start()
    
    def _Playsound(self,data):
        tmp = pydub.effects.speedup(self.audio[data],playback_speed=round(self.items['Entry'][data*3+2].get(),2)*0.05 + 1)
        self.length = tmp.duration_seconds
        play(tmp)
        self.now = [self.audionamelist[data],round(self.items['Entry'][data*3].get(),2),round(self.items['Entry'][data*3+1].get(),2),round(self.items['Entry'][data*3+2].get(),2)]
        self.textvar.set(self.now)
    
    def Play(self):
        if self.playline:
            self.playline = False
        else:
            self.playline = True
    
    def a(self,event,num):
        print(num,event)
        if num[1] == 0:
            self.audio[num[0]] = self.audio[num[0]] + (float(event) - self.sound[num[0]])
            self.sound[num[0]] = float(event)
    
    def InputLoading(self):
        for i in range(5):
            for j in range(3):
                self.items['Entry'].append(ttk.Scale(self.items['Text'][i],from_=10,to=-10,orient='vertical',command=lambda tmp,data=(i,j):self.a(tmp,data)))
                self.items['Entry'][-1].grid(row=0,column=j,padx=10,pady=10)
                self.items['Text'].append(ttk.Label(self.items['Text'][i],text=['音量','音调','速度'][j]))
                self.items['Text'][-1].grid(row=1,column=j,padx=10,pady=10)
        self.items['Entry'].append(ttk.Scale(self.tk,from_=0,to=10000,orient='horizontal',command=lambda tmp:self.innerline.place_configure(x=-(float(tmp)/10000)*1200),length=1200))
        self.items['Entry'][-1].grid(row=5,column=0,columnspan=5,padx=10,pady=10)
        self.line = ttk.Frame(self.tk,relief='sunken',borderwidth=2,width=1200,height=30)
        self.line.grid(row=4,column=0,columnspan=5,padx=10,pady=10)
        self.innerline = ttk.Frame(self.line)
        self.innerline.place(x=0,y=0,width=10000,height=30)
        self.innerline.bind('<ButtonPress-1>', self.place)
        self.ap = ttk.Label(self.line,background='black')
        self.ap.place(x=20,y=0,width=3,height=30)
        self.tk.after(10,self.innerlinemove)
    
    def innerlinemove(self):
        if self.playline:
            self.items['Entry'][-1].set(((-int(self.innerline.place_info()['x'])+1)/1200)*10000)
        if int(float(self.items['Entry'][-1].get())) == 10000:
            print(10000)
            self.playline = False
        self.tk.after(10,self.innerlinemove)

    def place(self,event):
        tmp = tk.Label(self.innerline,background='blue',fg='white',text=eval(self.textvar.get())[0],relief='raised',borderwidth=5)
        tmp.place(x=event.x,y=0,width=self.length*200,height=29)
        tmp.bind('<ButtonPress-3>', lambda n:tmp.destroy())
    
    def ButtonLoading(self):
        for i in range(5):
            self.items['Button'].append(ttk.Button(self.tk, text=self.audionamelist[i],width=20,command=lambda data=i:self.Playsound(data)))
            self.items['Button'][-1].grid(row=2,column=i,padx=20,pady=20)
        self.items['Button'].append(ttk.Button(self.tk, text='play',width=20,command=self.Play))
        self.items['Button'][-1].grid(row=3,column=0,columnspan = 5,padx=20,pady=20)
        
        # self.pp()
    
    def TextLoading(self):
        for i in range(5):
            self.items['Text'].append(ttk.Frame(self.tk,relief='sunken',borderwidth=1))
            self.items['Text'][-1].grid(row=1,column=i)
        self.items['Text'].append(ttk.Label(self.tk,textvariable=self.textvar))
        self.items['Text'][-1].grid(row=6,column=0,columnspan=5,padx=10,pady=10)
    
    def pp(self):
        print(self.items['Entry'][0].get())
        self.tk.after(10,self.pp)

a = Sound()
a.PrepareUILoading()
a.Mainloop()