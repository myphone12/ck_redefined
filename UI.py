import tkinter as tk
from tkinter import ttk, messagebox as msg

from reck import Ck

class _UI:

    def __init__(self):
        self.tk.iconbitmap('.\\icon.ico')
        self.tk.resizable(0,0)
        self.ck = Ck()
    
    def MenuLoading(self):
        pass

    def ButtonLoading(self):
        pass

    def TextLoading(self):
        pass

    def PrepareUILoading(self):
        self.MenuLoading()
        self.ButtonLoading()
        self.TextLoading()
    
    def Mainloop(self):
        self.tk.mainloop()


class main_UI(_UI):

    def __init__(self, set = 'default'):
        self.tk = tk.Tk()
        super().__init__()
        self.tk.title('Wish stimulator')

        self.WishDataVar = tk.StringVar()
    
    def OneWish(self):
        self.ck.ck()
        self.WishDataVar.set(str(self.ck))
    
    def TenWish(self):
        self.ck.ck(cishu= 10)
        self.WishDataVar.set(str(self.ck))
    
    def OpenSettings(self):
        self.SettingsPage = Settings_UI(self.tk)
        self.SettingsPage.PrepareUILoading()
    
    def MenuLoading(self):
        self.wish_mainmenu = tk.Menu(self.tk, tearoff=False)
        self.wish_menu1 = tk.Menu(self.wish_mainmenu, tearoff=False)
        self.wish_menu1.add_command(label='112', command=self.OneWish)
        self.wish_menu1.add_command(label='113', command=self.TenWish)
        self.wish_mainmenu.add_cascade(label='11', menu=self.wish_menu1)
        self.wish_mainmenu.add_command(label='112', command=self.OneWish)
        self.wish_mainmenu.add_command(label='Settings', command=self.OpenSettings)
        self.tk.config(menu=self.wish_mainmenu)
    
    def ButtonLoading(self):
        self.wish_button1 = ttk.Button(self.tk, text='One wish', width=10, command=self.OneWish)
        self.wish_button1.grid(row=2, column=1, padx=20, pady=10)
        self.wish_button2 = ttk.Button(self.tk, text='Ten wish', width=10, command=self.TenWish)
        self.wish_button2.grid(row=2, column=2, padx=20, pady=10)

    def TextLoading(self):
        self.wish_text1 = tk.Label(self.tk, width=80, height=10, 
                            textvariable = self.WishDataVar, anchor='s', 
                            font=("Microsoft Yahei UI", 9),fg='orange', 
                            wraplength=500, relief='sunken')
        self.wish_text1.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

        tk.Scrollbar

class Settings_UI(_UI):

    def __init__(self, TopLevel = False):
        if TopLevel:
            self.tk = tk.Toplevel(TopLevel)
        else:
            self.tk = tk.Tk()
        super().__init__()
        self.tk.title('Settings')
    
    def TextLoading(self):
        self.set_text1 = tk.Label(self.tk, text='选择数据库：')
        self.set_text1.grid(row=0, column=5)

        self.set_text2 = tk.Label(self.tk, text='五星概率：四星概率：五星小保底：五星大保底：四星小保底：四星大保底：')
        self.set_text2.grid(row=3, column=0)
    

    
