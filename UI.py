import tkinter as tk
from tkinter import ttk, messagebox as msg
from time import sleep
from PIL import Image, ImageTk
import threading, json, winsound, random, cv2, webbrowser,sys
from reck import Ck
import language

class _UI(language.language):

    def __init__(self, TopLevel = False):
        super().__init__()
        self.en_US()
        if TopLevel:
            self.tk = tk.Toplevel(TopLevel)
        else:
            self.tk = tk.Tk()
        self.tk.iconbitmap('.\\icon.ico')
        self.tk.resizable(0,0)
        screenwidth = self.tk.winfo_screenwidth()
        screenheight = self.tk.winfo_screenheight()
        self.tk.update()
        width = self.tk.winfo_width()
        height = self.tk.winfo_height()
        size = '+%d+%d' % ((screenwidth - width)/2, (screenheight - height)/2)
        self.tk.geometry(size)
        self.items = {'Text': [], 'Entry': [], 'Checkbox': [], 'Button': []}
        self.Varitems = {'TextVar': [], 'EntryVar': [], 'CheckboxVar': [], 'ButtonVar': []}
    
    def MenuLoading(self):
        pass

    def ButtonLoading(self):
        pass

    def TextLoading(self):
        pass

    def InputLoading(self):
        pass

    def Destroy(self):
        for i in self.items['Text']:
            i.destroy()
        for i in self.items['Entry']:
            i.destroy()
        for i in self.items['Checkbox']:
            i.destroy()
        for i in self.items['Button']:
            i.destroy()
        self.items = {'Text': [], 'Entry': [], 'Checkbox': [], 'Button': []}
        self.Varitems = {'TextVar': [], 'EntryVar': [], 'CheckboxVar': [], 'ButtonVar': []}
    
    def Reload(self):
        self.Destroy()
        self.PrepareUILoading()
        self.tk.update()


    def PrepareUILoading(self):
        self.MenuLoading()
        self.TextLoading()
        self.InputLoading()
        self.ButtonLoading()
    
    def Mainloop(self):
        self.tk.mainloop()


class main_UI(_UI):

    def __init__(self, TopLevel = False):
        super().__init__(TopLevel)
        self.ck = Ck()
        self.tk.title(self.lang.title)

        self.WishDataVar = tk.StringVar()
        self.wish_text2Var = tk.StringVar()
        self.easteregg = 0
    
    def OneWish(self):
        self.ck.ck()
        self.WishDataVar.set(str(self.ck))
    
    def TenWish(self):
        self.ck.ck(cishu= 10)
        self.WishDataVar.set(str(self.ck))
    
    def OpenSettings(self):
        self.SettingsPage = Settings_UI(self.tk)
        self.SettingsPage.PrepareUILoading()
    
    def EasterEgg(self):
        if not self.easteregg:
            msg.showinfo(self.lang.easteregg,self.lang.eastereggmsg)
            self.easteregg = 1
            match random.choice([0,1,2]):
                case 0:
                    self.wish_text2 = tk.Label(self.tk, textvariable=self.wish_text2Var, 
                                    font=('Microsoft Yahei UI', 9))
                    self.wish_text2.grid(row=2, column=0, columnspan=2, pady=10)
                    self.wish_text2_threading = threading.Thread(target=self._TextVar1, daemon=True)
                    self.wish_text2_threading.start()
                    self.tk.update()
                case 1:
                    self.video = Player(self.tk, '.\\src\\sddl.mp4', '说的道理')
                    self.wish_text2_threading = threading.Thread(target=self._video1, daemon=True)
                    self.wish_text2_threading.start()
                    self.video.PrepareUILoading()
                case 2:
                    webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7/')
    
    def _video1(self):
        while True:
            if self.video.finish == 1:
                image = Player(self.tk, '.\\src\\wow.mp4', '袜袄！！！' , '+0+0')
                image.PrepareUILoading()
                break

    def _TextVar1(self):
        while True:
            self.wish_text2Var.set('( ^ _ ^ )')
            sleep(2)
            self.wish_text2Var.set('( *^▽^* )')
            sleep(2)
            self.wish_text2Var.set('ヾ(✿ﾟ▽ﾟ)ノ')
            sleep(2)
            self.wish_text2Var.set('(ﾉ≧∀≦)ﾉ')
            sleep(2)
            self.wish_text2Var.set('(oﾟ▽ﾟ)o  ')
            sleep(2)

    def MenuLoading(self):
        self.wish_mainmenu = tk.Menu(self.tk, tearoff=False)
        self.wish_menu1 = tk.Menu(self.wish_mainmenu, tearoff=False)
        self.wish_menu1.add_command(label='112', command=self.OneWish)
        self.wish_menu1.add_command(label='113', command=self.TenWish)
        self.wish_mainmenu.add_cascade(label='11', menu=self.wish_menu1)
        self.wish_mainmenu.add_command(label='112', command=self.OneWish)
        self.wish_mainmenu.add_command(label=self.lang.settings, command=self.OpenSettings)
        self.wish_mainmenu.add_command(label='  ', command=self.EasterEgg)
        self.tk.config(menu=self.wish_mainmenu)
    
    def ButtonLoading(self):
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.onewish, width=10, command=self.OneWish))
        self.items['Button'][-1].grid(row=1, column=0, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.tenwish, width=10, command=self.TenWish))
        self.items['Button'][-1].grid(row=1, column=1, padx=20, pady=10)

    def TextLoading(self):
        self.Varitems['TextVar'].append(tk.StringVar())
        self.items['Text'].append(tk.Label(self.tk, width=80, height=10, 
                            textvariable = self.Varitems['TextVar'][-1], anchor='s', 
                            font=("Microsoft Yahei UI", 9),fg='orange', 
                            wraplength=500, relief='sunken'))
        self.items['Text'][-1].grid(row=0, column=0, columnspan=2, padx=20, pady=10)
    
class Settings_UI(_UI):

    def __init__(self, TopLevel = False):
        super().__init__(TopLevel)
        self.tk.title(self.lang.settings)

        with open('.\\database.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            self.database = self.data['default']
            self.CurrentData = 'default'
    
    def About(self):
        pass

    def SaveChange(self):
        tmp = 0;n = 1
        for i in self.database['data']:
            n += 1
            for j in self.database['data'][i]:
                tmp += 1
                if j == '保底':
                    if not self.Varitems['CheckboxVar'][int(tmp - n)].get():
                        self.data[self.CurrentData]['data'][i]['保底'] = '0'
                        continue
                if j == '大保底':
                    if not self.Varitems['CheckboxVar'][int(tmp - n)].get():
                        self.data[self.CurrentData]['data'][i]['大保底'] = '0'
                        continue
                self.data[self.CurrentData]['data'][i][j] = self.Varitems['EntryVar'][tmp - 1].get()
            
            
        with open('.\\database.json', 'w+', encoding='utf-8') as file:
            file.write(json.dumps(self.data, ensure_ascii=False, indent=4))

    def setDB(self,database):
        self.CurrentData = database
        self.database = self.data.get(database)
        self.Reload()
    
    def delDB(self):
        n = msg.askokcancel(title=self.lang.deletedb, message=self.lang.deletedbmsg)

    def ChangeItemData(self):
        self.ChangeItemDataWindow = ItemDataSettings_UI(TopLevel= self.tk, data=self.CurrentData)
        self.ChangeItemDataWindow.PrepareUILoading()

    def newDB(self):
        self.CreateNewWindow = CreateNewWindow(self.tk, self.lang.newdb)
        self.CreateNewWindow.PrepareUILoading()

    def setLanguage(self,language):
        print(language)
    
    def CreateNew(self):
        self.CreateNewWindow = CreateNewWindow(self.tk, self.lang.newitem)
        self.rename_thread = threading.Thread(target=lambda:self._CreateNew())
        self.rename_thread.start()
        self.CreateNewWindow.PrepareUILoading()

    def Del(self, data):
        n = msg.askokcancel(title=self.lang.deleteitem, message=self.lang.deleteitemmsg)
        if n and len(self.data[self.CurrentData]['data']) > 1:
            tmp = {}
            for i in self.data[self.CurrentData]['data']:
                if i == data:
                       pass
                else:
                    tmp[i] = self.data[self.CurrentData]['data'][i]
            del self.data[self.CurrentData]['data']
            self.data[self.CurrentData]['data'] = tmp
            del self.database['data']
            self.database['data'] = tmp
            self.Reload()
            self.SaveChange()
        elif len(self.data[self.CurrentData]['data']) <= 1:
            msg.showerror('提示','必须保留至少一项！')

    def Rename(self, data):
        self.CreateNewWindow = CreateNewWindow(self.tk, self.lang.rename,data)
        self.rename_thread = threading.Thread(target=lambda:self._Rename(data))
        self.rename_thread.start()
        self.CreateNewWindow.PrepareUILoading()
        
        
    def _Rename(self, data):
        tmp = {}
        while True:
            if self.CreateNewWindow.ReturnData != '' and self.CreateNewWindow.ReturnData != '0':
                for i in self.data[self.CurrentData]['data']:
                    if i == data:
                        tmp[self.CreateNewWindow.ReturnData] = self.data[self.CurrentData]['data'][i]
                    else:
                        tmp[i] = self.data[self.CurrentData]['data'][i]
                del self.data[self.CurrentData]['data']
                self.data[self.CurrentData]['data'] = tmp
                del self.database['data']
                self.database['data'] = tmp
                self.CreateNewWindow.ReturnData = ''
                self.Reload()
                self.SaveChange()
                break
            if self.CreateNewWindow.ReturnData == '0':
                break

    def _CreateNew(self):
        tmp = {}
        while True:
            if self.CreateNewWindow.ReturnData != '' and self.CreateNewWindow.ReturnData != '0':
                for i in self.data[self.CurrentData]['data']:
                    tmp[i] = self.data[self.CurrentData]['data'][i]
                tmp[self.CreateNewWindow.ReturnData] = {'概率': '0', '保底': '0', '大保底': 0}
                del self.data[self.CurrentData]['data']
                self.data[self.CurrentData]['data'] = tmp
                del self.database['data']
                self.database['data'] = tmp
                self.Reload()
                self.SaveChange()
                break
            if self.CreateNewWindow.ReturnData == '0':
                break
    
    def TextLoading(self):
        for i in range(len(self.database['data'])):
            self.items['Text'].append(tk.Label(self.tk, text=list(self.database['data'].keys())[i] + '概率:'))
            self.items['Text'][i].grid(row=i+2, column=0, padx=5, pady=5)

        # self.items['Text']3 = tk.Label(self.tk, text='五星Up；  四星Up：')
        # self.items['Text']3.grid(row=8, column=0)
    
    def MenuLoading(self):
        self.set_mainmenu = tk.Menu(self.tk, tearoff=False)
        self.set_menu1 = tk.Menu(self.set_mainmenu, tearoff=False)
        for i in self.data.keys():
            self.set_menu1.add_command(label=i, command=lambda data=i:self.setDB(data))
        self.set_menu1.add_separator()
        self.set_menu1.add_command(label=self.lang.newdb, command=self.newDB)
        self.set_menu2 = tk.Menu(self.set_mainmenu, tearoff=False)
        self.set_menu2.add_command(label='zh_CN', command=lambda:self.setLanguage('zh_CN'))
        self.set_menu2.add_command(label='en_US', command=lambda:self.setLanguage('en_US'))
        self.set_mainmenu.add_cascade(label=self.lang.choosedb, menu=self.set_menu1)
        self.set_mainmenu.add_cascade(label=self.lang.chooselang, menu=self.set_menu2)
        self.set_mainmenu.add_command(label=self.lang.about, command=self.About)
        self.tk.config(menu=self.set_mainmenu)

    def InputLoading(self):
        tmp = 2
        for i in self.database['data']:
            self.Varitems['EntryVar'].append(tk.StringVar())
            self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=8))
            self.items['Entry'][-1].grid(row=tmp, column=1, padx=5)
            self.Varitems['EntryVar'][-1].set(str(self.database['data'][i]['概率']))
            self.Varitems['EntryVar'].append(tk.StringVar())
            self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=5))
            self.items['Entry'][-1].grid(row=tmp, column=3, padx=5)
            self.Varitems['EntryVar'][-1].set(str(self.database['data'][i]['保底']))
            self.Varitems['EntryVar'].append(tk.StringVar())
            self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=5))
            self.items['Entry'][-1].grid(row=tmp, column=5, padx=10)
            self.Varitems['EntryVar'][-1].set(str(self.database['data'][i]['大保底']))
            self.Varitems['CheckboxVar'].append(tk.IntVar())
            self.items['Checkbox'].append(ttk.Checkbutton(self.tk, text='小保底', variable=self.Varitems['CheckboxVar'][-1]))
            self.items['Checkbox'][-1].grid(row=tmp, column=2, padx=10)
            self.Varitems['CheckboxVar'][-1].set(bool(self.database['data'][i]['保底'] != '0'))
            self.Varitems['CheckboxVar'].append(tk.IntVar())
            self.items['Checkbox'].append(ttk.Checkbutton(self.tk, text='大保底', variable=self.Varitems['CheckboxVar'][-1]))
            self.items['Checkbox'][-1].grid(row=tmp, column=4, padx=10)
            self.Varitems['CheckboxVar'][-1].set(bool(self.database['data'][i]['大保底'] != '0'))
            tmp += 1
        self.finalcloumn = tmp
        
    def ButtonLoading(self):
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.setitemdata, width=20, command=self.ChangeItemData))
        self.items['Button'][-1].grid(row=0, column=0, columnspan=3, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.save, width=20, command=self.SaveChange))
        self.items['Button'][-1].grid(row=0, column=3, columnspan=3, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.deletedb, width=20, command=self.delDB))
        self.items['Button'][-1].grid(row=0, column=6, columnspan=2, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.newitem, width=40, command=self.CreateNew))
        self.items['Button'][-1].grid(row=self.finalcloumn, column=0, columnspan=8, padx=20, pady=10)
        for i in self.database['data']:
            self.items['Button'].append(ttk.Button(self.tk, text=self.lang.rename, command=lambda data=i:self.Rename(data)))
            self.items['Button'][-1].grid(row=list(self.database['data'].keys()).index(i) + 2, column=6, padx=10)
            self.items['Button'].append(ttk.Button(self.tk, text=self.lang.deleteitem, command=lambda data=i:self.Del(data)))
            self.items['Button'][-1].grid(row=list(self.database['data'].keys()).index(i) + 2, column=7, padx=10)

class CreateNewWindow(_UI):

    def __init__(self, TopLevel = False, title = 'New', varset = ''):
        super().__init__(TopLevel)
        self.tk.title(title)
        self.varset = varset
        self.ReturnData = ''
    
    def Save(self):
        self.ReturnData = self.Varitems['TextVar'][-1].get()
        self.tk.destroy()
    
    def Cancel(self):
        self.ReturnData = '0'
        self.tk.destroy()

    def TextLoading(self):
        self.items['Text'].append(ttk.Label(self.tk, text=self.lang.setname))
        self.items['Text'][-1].grid(row=0, column=0,columnspan=2)
        self.Varitems['TextVar'].append(tk.StringVar())
        self.items['Text'].append(ttk.Entry(self.tk, textvariable=self.Varitems['TextVar'][-1], width=20))
        self.items['Text'][-1].grid(row=1, column=0,columnspan=2, padx=10, pady=10)
        self.Varitems['TextVar'][-1].set(self.varset)
    
    def ButtonLoading(self):
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.save, width=20, command=self.Save))
        self.items['Button'][-1].grid(row=2, column=1, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.cancel, width=20, command=self.Cancel))
        self.items['Button'][-1].grid(row=2, column=0, padx=20, pady=10)

class Player(_UI):

    def __init__(self, TopLevel=False, playitem = '', title = '', pos = 0):
        super().__init__(TopLevel)
        self.tk.title(title)
        self.playitem = playitem
        self.tk.protocol("WM_DELETE_WINDOW", self.on_closing)
        if pos:
            self.tk.geometry(pos)
        self.finish = 0

    def on_closing(self):
        self.tk.destroy()
        self.finish = 1
        sys.exit()

    def play_video(self):
        self.cap = cv2.VideoCapture(self.playitem)
    
    def play_image(self):
        self.img = cv2.imread(self.playitem)
        tmp = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(tmp)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        self.tk.update()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk  
            self.label.configure(image=imgtk)
            self.label.after(5, self.update_frame)
        else:
            self.cap.release()
            self.finish = 1
            self.tk.destroy()
    
    def TextLoading(self):
        self.label = ttk.Label(self.tk)
        self.label.grid(padx=10, pady=10)
        if self.playitem[-3:-1] == 'jp':
            self.play_image()
            winsound.PlaySound(self.playitem[0:-3] + 'wav',winsound.SND_ASYNC or winsound.SND_FILENAME)
        elif self.playitem[-3:-1] == 'mp':
            self.play_video()
            winsound.PlaySound(self.playitem[0:-3] + 'wav',winsound.SND_ASYNC or winsound.SND_FILENAME)
            self.update_frame()
        
class ItemDataSettings_UI(_UI):

    def __init__(self, TopLevel=False, data = 'default'):
        super().__init__(TopLevel)

        self.tk.title(self.lang.setitemdata)
        with open('.\\database.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            self.database = self.data[data]
            self.CurrentData = data
    
    def Save(self):
        pass

    def TextLoading(self):
        for i in range(len(self.database) - 1):
            self.items['Text'].append(tk.Label(self.tk, text=list(self.database.keys())[i] + ':'))
            self.items['Text'][i].grid(row=i, column=0, padx=5, pady=5)
    
    def InputLoading(self):
        tmp = 0
        for i in self.database:
            if i != 'data':
                self.Varitems['EntryVar'].append(tk.StringVar())
                self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=80))
                self.items['Entry'][-1].grid(row=tmp, column=1, padx=10)
                self.Varitems['EntryVar'][-1].set(str(self.database[i])[1:-1])
            tmp += 1
        self.finalcolumn = tmp
    
    def ButtonLoading(self):
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.save, width=80, command=self.Save))
        self.items['Button'][-1].grid(row=self.finalcolumn + 1, column=0, columnspan=2, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.cancel, width=80, command=self.tk.destroy))
        self.items['Button'][-1].grid(row=self.finalcolumn + 2, column=0, columnspan=2, padx=20, pady=10)