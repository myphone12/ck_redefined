import tkinter as tk
from tkinter import ttk, messagebox as msg
from time import sleep
import threading, json

from reck import Ck
from copy import copy

class _UI:

    def __init__(self):
        self.tk.iconbitmap('.\\icon.ico')
        self.tk.resizable(0,0)
    
    def MenuLoading(self):
        pass

    def ButtonLoading(self):
        pass

    def TextLoading(self):
        pass

    def InputLoading(self):
        pass

    def PrepareUILoading(self):
        self.MenuLoading()
        self.TextLoading()
        self.InputLoading()
        self.ButtonLoading()
    
    def Mainloop(self):
        self.tk.mainloop()


class main_UI(_UI):

    def __init__(self, set = 'default'):
        self.tk = tk.Tk()
        self.ck = Ck()
        super().__init__()
        self.tk.title('Wish stimulator')

        self.WishDataVar = tk.StringVar()
        self.wish_text2Var = tk.StringVar()
    
    def OneWish(self):
        self.ck.ck()
        self.WishDataVar.set(str(self.ck))
    
    def TenWish(self):
        self.ck.ck(cishu= 10)
        self.WishDataVar.set(str(self.ck))
    
    def OpenSettings(self):
        self.SettingsPage = Settings_UI(self.tk)
        self.SettingsPage.PrepareUILoading()
    
    def _TextVar1(self):
        while True:
            self.wish_text2Var.set('( ^ _ ^ )')
            sleep(2)
            self.wish_text2Var.set('( *^▽^* )')
            sleep(2)

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
        self.wish_button1.grid(row=1, column=0, padx=20, pady=10)
        self.wish_button2 = ttk.Button(self.tk, text='Ten wish', width=10, command=self.TenWish)
        self.wish_button2.grid(row=1, column=1, padx=20, pady=10)

    def TextLoading(self):
        self.wish_text1 = tk.Label(self.tk, width=80, height=10, 
                            textvariable = self.WishDataVar, anchor='s', 
                            font=("Microsoft Yahei UI", 9),fg='orange', 
                            wraplength=500, relief='sunken')
        self.wish_text1.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.wish_text2 = tk.Label(self.tk, textvariable=self.wish_text2Var, 
                            font=('Microsoft Yahei UI', 9))
        self.wish_text2.grid(row=2, column=0, columnspan=2, pady=10)
        self.wish_text2_threading = threading.Thread(target=self._TextVar1, daemon=True)
        self.wish_text2_threading.start()

class Settings_UI(_UI):

    def __init__(self, TopLevel = False):
        if TopLevel:
            self.tk = tk.Toplevel(TopLevel)
        else:
            self.tk = tk.Tk()
        super().__init__()
        self.tk.title('Settings')

        with open('.\\database.json', 'r', encoding='utf-8') as file:
            self.data = json.loads(file)
            self.database = self.data['default']
            self.CurrentData = 'default'

        self.set_text = []
        self.set_entry = []
        self.set_checkbox = []
        self.EntryVar = []
        self.CheckboxVar = []
    
    def About(self):
        pass

    def SaveChange(self):
        tmp = 0
        for i in self.database['data']:
            for j in self.database['data'][i]:
                self.data[self.CurrentData]['data'][i][j] = self.EntryVar[tmp].get()
                tmp += 1
        with open('.\\database.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.data))
        

    def setDB(self,database):
        self.CurrentData = database
        self.database = self.data.get(database)
        self.Reload()
        

    def setLanguage(self,language):
        print(language)
    
    def Reload(self):
        for i in self.set_text:
            i.destroy()
        for i in self.set_entry:
            i.destroy()
        for i in self.set_checkbox:
            i.destroy()
        self.set_text = []
        self.set_entry = []
        self.set_checkbox = []
        self.CheckboxVar = []
        self.EntryVar = []
        self.PrepareUILoading()
        self.tk.update()

    def TextLoading(self):
        for i in range(len(self.database['data'])):
            self.set_text.append(tk.Label(self.tk, text=list(self.database['data'].keys())[i] + '概率:'))
            self.set_text[i].grid(row=i+2, column=0, padx=5, pady=5)

        # self.set_text3 = tk.Label(self.tk, text='五星Up；  四星Up：')
        # self.set_text3.grid(row=8, column=0)
    
    def MenuLoading(self):
        self.set_mainmenu = tk.Menu(self.tk, tearoff=False)
        self.set_menu1 = tk.Menu(self.set_mainmenu, tearoff=False)
        for i in self.data.keys():
            self.set_menu1.add_command(label=i, command=lambda data=i:self.setDB(data))
        self.set_menu2 = tk.Menu(self.set_mainmenu, tearoff=False)
        self.set_menu2.add_command(label='zh_CN', command=lambda:self.setLanguage('zh_CN'))
        self.set_menu2.add_command(label='en_US', command=lambda:self.setLanguage('en_US'))
        self.set_mainmenu.add_cascade(label='选择数据库', menu=self.set_menu1)
        self.set_mainmenu.add_cascade(label='设置语言', menu=self.set_menu2)
        self.set_mainmenu.add_command(label='关于', command=self.About)
        self.tk.config(menu=self.set_mainmenu)

    def InputLoading(self):
        tmp = 2
        for i in self.database['data']:
            self.EntryVar.append(tk.StringVar())
            self.set_entry.append(ttk.Entry(self.tk, textvariable=self.EntryVar[-1], width=8))
            self.set_entry[-1].grid(row=tmp, column=1, padx=5)
            self.EntryVar[-1].set(value = str(self.database['data'][i]['概率']))
            self.EntryVar.append(tk.StringVar())
            self.set_entry.append(ttk.Entry(self.tk, textvariable=self.EntryVar[-1], width=5))
            self.set_entry[-1].grid(row=tmp, column=3, padx=5)
            self.EntryVar[-1].set(value = str(self.database['data'][i]['保底']))
            self.EntryVar.append(tk.StringVar())
            self.set_entry.append(ttk.Entry(self.tk, textvariable=self.EntryVar[-1], width=5))
            self.set_entry[-1].grid(row=tmp, column=5, padx=10)
            self.EntryVar[-1].set(value = str(self.database['data'][i]['大保底']))
            self.CheckboxVar.append(tk.IntVar())
            self.set_checkbox.append(ttk.Checkbutton(self.tk, text='小保底', variable=self.CheckboxVar[-1]))
            self.set_checkbox[-1].grid(row=tmp, column=2, padx=10)
            self.CheckboxVar[-1].set(value = bool(self.database['data'][i]['保底']))
            self.CheckboxVar.append(tk.IntVar())
            self.set_checkbox.append(ttk.Checkbutton(self.tk, text='大保底', variable=self.CheckboxVar[-1]))
            self.set_checkbox[-1].grid(row=tmp, column=4, padx=10)
            self.CheckboxVar[-1].set(value = bool(self.database['data'][i]['大保底']))
            tmp += 1
        self.finalcloumn = tmp
        
    def ButtonLoading(self):
        self.set_button1 = ttk.Button(self.tk, text='修改抽卡物品数据', width=20, command=self.SaveChange)
        self.set_button1.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
        self.set_button2 = ttk.Button(self.tk, text='保存', width=20, command=self.SaveChange)
        self.set_button2.grid(row=0, column=3, columnspan=3, padx=20, pady=10)
        self.set_button2 = ttk.Button(self.tk, text='新建', width=40, command=self.SaveChange)
        self.set_button2.grid(row=self.finalcloumn, column=3, columnspan=6, padx=20, pady=10)