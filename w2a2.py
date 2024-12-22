import wave,pydub,ctypes,threading
from pydub.playback import play
import tkinter as tk
from tkinter import ttk , messagebox as msg
from UI import _UI

# class inner
class Sound(_UI):

    def __init__(self):
        super().__init__()
        self.textvar = tk.StringVar()
        ctypes.windll.shell32.IsUserAnAdmin()
        self.audio = [pydub.AudioSegment.from_wav(i) for i in ['5.wav','鹅.wav','啊.wav','鹅2.wav','er.wav']]
        self.sound = [0,0,0,0,0]
    
    def Playsound(self,data):
        self.thread = threading.Thread(target=lambda:self._Playsound(data))
        self.thread.start()
    
    def _Playsound(self,data):
        play(self.audio[data])
        self.textvar.set('(' + ['5','鹅','啊','鹅','er'][data] + ', ' + str(round(self.items['Entry'][data*3].get(),2)) + ', ' + str(round(self.items['Entry'][data*3+1].get(),2)) + ', ' + str(round(self.items['Entry'][data*3+2].get(),2)) + ')')

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
    
    def ButtonLoading(self):
        for i in range(5):
            self.items['Button'].append(ttk.Button(self.tk, text=['5','鹅','啊','鹅','er'][i],width=20,command=lambda data=i:self.Playsound(data)))
            self.items['Button'][-1].grid(row=2,column=i,padx=20,pady=20)
        
        # self.pp()
    
    def TextLoading(self):
        for i in range(5):
            self.items['Text'].append(ttk.Frame(self.tk,relief='sunken',borderwidth=1))
            self.items['Text'][-1].grid(row=1,column=i)
        self.items['Text'].append(ttk.Label(self.tk,textvariable=self.textvar))
        self.items['Text'][-1].grid(row=3,column=0,columnspan=5,padx=10,pady=10)
    
    def pp(self):
        print(self.items['Entry'][0].get())
        self.tk.after(10,self.pp)

a = Sound()
a.PrepareUILoading()
a.Mainloop()