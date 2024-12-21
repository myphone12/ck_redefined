import wave,winsound,librosa
import tkinter as tk
from tkinter import ttk , messagebox as msg
from UI import _UI

# class inner
class Sound(_UI):

    def __init__(self):
        super().__init__()

    def InputLoading(self):
        for i in range(4):
            for j in range(3):
                self.items['Entry'].append(ttk.Scale(self.items['Text'][i],from_=100,to=0,orient='vertical'))
                self.items['Entry'][-1].grid(row=0,column=j,padx=10,pady=10)
    
    def ButtonLoading(self):
        self.button1 = ttk.Button(self.tk, text='5',width=20)
        self.button1.grid(row=2,column=0,padx=20,pady=20)
        self.button2 = ttk.Button(self.tk, text='鹅',width=20)
        self.button2.grid(row=2,column=1,padx=20,pady=20)
        self.button3 = ttk.Button(self.tk, text='啊',width=20)
        self.button3.grid(row=2,column=2,padx=20,pady=20)
        self.button4 = ttk.Button(self.tk,text='鹅',width=20)
        self.button4.grid(row=2,column=3,padx=20,pady=20)
        
        self.pp()
    
    def TextLoading(self):
        for i in range(4):
            self.items['Text'].append(ttk.Frame(self.tk,relief='sunken',borderwidth=1))
            self.items['Text'][-1].grid(row=1,column=i)
    
    def pp(self):
        print(self.items['Entry'][0].get())
        self.tk.after(10,self.pp)

a = Sound()
a.PrepareUILoading()
a.Mainloop()