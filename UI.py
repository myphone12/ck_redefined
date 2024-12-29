import tkinter as tk
from tkinter import ttk, messagebox as msg
from PIL import Image, ImageTk
import json, winsound, random, cv2, webbrowser, sys, math, ctypes
from reck import Ck, DataLoading
from innerwindow import InnerWindow
from test import TestFun
import language

class _UI(DataLoading):

    def __init__(self, TopLevel = False, dataload = False,Test = False):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        self.isopen = True
        self.istest = False
        self.drag_start_x = None
        self.drag_start_y = None
        self.dataloadflag = dataload
        if dataload:
            super().__init__(dataload)
        self.lang = language.language()
        with open('.\\language', 'r') as l:
            tmp = l.read()
            if tmp == 'zh_CN':
                self.lang.zh_CN()
            elif tmp == 'en_US':
                self.lang.en_US()
        if TopLevel:
            self.tk = tk.Toplevel(TopLevel)
        else:
            self.tk = tk.Tk()
        self.tk.iconbitmap('.\\src\\icon.ico')
        self.tk.resizable(0,0)
        screenwidth = self.tk.winfo_screenwidth()
        screenheight = self.tk.winfo_screenheight()
        width = self.tk.winfo_width()
        height = self.tk.winfo_height()
        size = '+%d+%d' % ((screenwidth - width)/2, (screenheight - height)/2)
        self.tk.geometry(size)
        self.tk.protocol("WM_DELETE_WINDOW", self._close)
        self.mover = tk.Frame(self.tk, width=2000, height=2000)
        self.mover.place(x=0,y=0)
        self.mover.bind('<ButtonPress-1>', self.on_drag_start)
        self.mover.bind('<B1-Motion>', self.on_drag_motion)
        self.mover.bind('<ButtonRelease-1>', self.on_drag_release)
        self.items = {'Text': [], 'Entry': [], 'Checkbox': [], 'Button': []}
        self.Varitems = {'TextVar': [], 'EntryVar': [], 'CheckboxVar': [], 'ButtonVar': []}
        if Test:
            self.Test = True
            self.innerwindow = InnerWindow(self.tk,'Console')
            self.innerwindow.showtext('Running...')
            self.tk.bind('<KeyPress-F11>',lambda a:self.ShowConsole())
            self.tk.bind('<KeyPress-C>',lambda a:self.innerwindow.clear())
            self.tk.bind('<KeyPress-c>',lambda a:self.innerwindow.clear())
            self.innerwindow.hide()
        else:
            self.Test = False
    
    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def on_drag_motion(self, event):
        print(end='')
        x = self.tk.winfo_x() - self.drag_start_x + event.x
        y = self.tk.winfo_y() - self.drag_start_y + event.y
        self.tk.geometry('+{0}+{1}'.format(x, y))
    
    def on_drag_release(self, event):
        self.drag_start_x = None
        self.drag_start_y = None

    def _close(self):
        self.isopen = False
        self.tk.destroy()
    
    def Move(self, speed = 2, agnle = math.pi/4):
        x = self.tk.winfo_x()
        y = self.tk.winfo_y()
        xdistance = speed
        ydistance = speed
        self.tk.after(10,self._Move,speed,agnle,x,y,xdistance,ydistance)

    def _Move(self, speed, agnle, x, y, xdistance, ydistance):
        try:
            if not self.drag_start_x:  
                x += xdistance
                y += int(ydistance*math.tan(agnle))
                self.tk.geometry(f'+{x}+{y}')
                self.tk.update()
                if self.tk.winfo_x() >= self.tk.winfo_screenwidth() - self.tk.winfo_width() or self.tk.winfo_x() <= 0:
                    xdistance = -xdistance
                if self.tk.winfo_y() >= self.tk.winfo_screenheight() - self.tk.winfo_height() or self.tk.winfo_y() <= 0:
                    ydistance = -ydistance
                if not self.isopen:
                    return 1
        except:
            pass
        self.tk.after(10,self._Move,speed,agnle,x,y,xdistance,ydistance)
    
    def ShowConsole(self):
        if self.Test and not self.innerwindow.isopen:
            self.innerwindow.show()
        

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
        if self.Test and self.innerwindow.isopen:
            self.innerwindow.show()

    def Mainloop(self):
        self.tk.mainloop()


class main_UI(_UI):

    def __init__(self, TopLevel = False):
        super().__init__(TopLevel, dataload = 'default',Test=True)
        self.ck = Ck()
        self.tk.title(self.lang.title)

        self.WishDataVar = tk.StringVar()
        self.wish_text2Var = tk.StringVar()
        self.easteregg = 0
        self.updateflag = 0
        self.tk.after(10,self._Settingwindowmonitor)
    
    def _Settingwindowmonitor(self):
        try:
            if not self.SettingsPage.isopen:
                if self.updateflag == 0:
                    self.Loadjson()
                    self.ChooseDB('default')
                    self.ck.Reload()
                    self.Reload()
                    self.updateflag = 1
            else:
                self.updateflag = 0
        except:
            pass
        self.tk.after(10,self._Settingwindowmonitor)
    @TestFun
    def OneWish(self):
        tmp = self.ck.ck()
        l = list(self.ck.database['data'].keys())
        tmp1 = self.Varitems['TextVar'][l.index(tmp[0][1])+1].get()
        self.Varitems['TextVar'][0].set(str(self.ck))
        tmp1 += tmp[0][0] + ', '
        self.Varitems['TextVar'][l.index(tmp[0][1])+1].set(tmp1)
        self.Varitems['TextVar'][-1].set(self.ck.TimesDB['all'])

    @TestFun
    def TenWish(self):
        tmp = self.ck.ck(cishu= 10)
        l = list(self.ck.database['data'].keys())
        tmp1 = []
        for i in range(len(l)):
            tmp1.append(self.Varitems['TextVar'][i+1].get())
        self.Varitems['TextVar'][0].set(str(self.ck))
        for i in tmp:
            tmp1[l.index(i[1])] += i[0] + ', '
        for i in range(len(l)):
            tmp1.append(self.Varitems['TextVar'][i+1].set(tmp1[i]))
        self.Varitems['TextVar'][-1].set(self.ck.TimesDB['all'])

    @TestFun
    def OpenSettings(self):
        try:
            if not self.SettingsPage.isopen:
                self.SettingsPage = Settings_UI(self.tk)
                self.SettingsPage.PrepareUILoading()
        except AttributeError:
            self.SettingsPage = Settings_UI(self.tk)
            self.SettingsPage.PrepareUILoading()
        except:
            pass
    @TestFun
    def ChooseDB(self, data):
        self.ck = Ck(set= data)
        self.Reload()
    @TestFun
    def EasterEgg(self):
        if not self.easteregg:
            msg.showinfo(self.lang.easteregg,self.lang.eastereggmsg)
            self.easteregg = 1
            match random.choice([0, 1, 2]):
                case 0:
                    self.text2 = tk.Label(self.tk, textvariable=self.wish_text2Var, 
                                    font=('Microsoft Yahei UI', 9))
                    self.text2.grid(row=len(self.ck.database['data'])*2 + 2, column=2, columnspan=2, pady=10)
                    self.tk.after(10,self._TextVar1,0)
                    self.tk.update()
                case 1:
                    self.video = Player(self.tk, '.\\src\\sddl.mp4', self.lang.sddl)
                    self.video.PrepareUILoading()
                    self.tk.after(10,self._video1)
                    self.Move(random.randint(1,10),random.random()*(math.pi/2))
                    self.video.Move(random.randint(1,10),random.random()*(math.pi/2))
                    try:
                        if self.SettingsPage:
                            self.SettingsPage.Move(random.randint(1,10),random.random()*(math.pi/2))
                    except:
                        pass
                case 2:
                    webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7/')
    
    def _video1(self):
        if self.video.finish == 1:
            image = Player(self.tk, '.\\src\\wow.mp4', self.lang.wow , '+0+0')
            image.PrepareUILoading()
        else:
            self.tk.after(10,self._video1)

    def _TextVar1(self,i):
            match i:
                case 0:
                    self.wish_text2Var.set('( ^ _ ^ )')
                    self.tk.after(2000,self._TextVar1,1)
                case 1:
                    self.wish_text2Var.set('( *^▽^* )')
                    self.tk.after(2000,self._TextVar1,2)
                case 2:
                    self.wish_text2Var.set('ヾ(✿ﾟ▽ﾟ)ノ')
                    self.tk.after(2000,self._TextVar1,3)
                case 3:
                    self.wish_text2Var.set('(ﾉ≧∀≦)ﾉ')
                    self.tk.after(2000,self._TextVar1,4)
                case 4:
                    self.wish_text2Var.set('(oﾟ▽ﾟ)o  ')
                    self.tk.after(2000,self._TextVar1,0)

    def MenuLoading(self):
        self.wish_mainmenu = tk.Menu(self.tk, tearoff=False)
        self.wish_menu1 = tk.Menu(self.wish_mainmenu, tearoff=False)
        for i in self.data.keys():
            self.wish_menu1.add_command(label=i, command=lambda data=i:self.ChooseDB(data))
        self.wish_mainmenu.add_cascade(label=self.lang.choosedb, menu=self.wish_menu1,underline=0)
        self.wish_mainmenu.add_command(label=self.lang.settings, command=self.OpenSettings,underline=1)
        self.wish_mainmenu.add_command(label='  ', command=self.EasterEgg,underline=2)
        self.tk.config(menu=self.wish_mainmenu)
    
    def ButtonLoading(self):
        tmp = len(self.ck.database['data'])*2 + 1
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.onewish, width=10, command=self.OneWish))
        self.items['Button'][-1].grid(row=tmp, column=0, columnspan=2, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.tenwish, width=10, command=self.TenWish))
        self.items['Button'][-1].grid(row=tmp, column=2, columnspan=2, padx=20, pady=10)

    def TextLoading(self):
        self.Varitems['TextVar'].append(tk.StringVar())
        self.items['Text'].append(tk.Label(self.tk, width=80, height=10, 
                            textvariable = self.Varitems['TextVar'][-1], anchor='s', 
                            font=("Microsoft Yahei UI", 9),fg='orange', 
                            wraplength=500, relief='sunken'))
        self.items['Text'][-1].grid(row=0, column=0, columnspan=4, padx=20, pady=10)
        for i in range(len(self.ck.database['data'])):
            self.items['Text'].append(tk.Label(self.tk, text=list(self.ck.database['data'].keys())[i] + ' :'))
            self.items['Text'][-1].grid(row=i+1, column=0, padx=5, pady=5)
            self.Varitems['TextVar'].append(tk.StringVar())
            self.items['Text'].append(tk.Label(self.tk, width=60, height=3, 
                                textvariable = self.Varitems['TextVar'][-1], anchor='s', 
                                font=("Microsoft Yahei UI", 9),fg='orange', 
                                wraplength=500, relief='sunken'))
            self.items['Text'][-1].grid(row=i+1, column=1, columnspan=3, padx=20, pady=10)
        self.Varitems['TextVar'].append(tk.StringVar())
        self.items['Text'].append(tk.Label(self.tk, textvariable = self.Varitems['TextVar'][-1]))
        self.items['Text'][-1].grid(row=len(self.ck.database['data'])*2 + 2, column=0,columnspan=4, padx=5, pady=5)
        try:
            if self.text2:
                self.text2.grid_configure(row=len(self.ck.database['data'])*2 + 2)
        except:
            pass
            

    
class Settings_UI(_UI):

    def __init__(self, TopLevel = False):
        super().__init__(TopLevel, dataload = 'default',Test=True)
        self.tk.title(self.lang.settings)
        self.isdel = 0
        self.about_isopen = 0
        self.isdeldb = 0
    @TestFun
    def SaveChange(self):
        tmp = list(range(len(self.Varitems['EntryVar'])))
        for i in range(0,len(self.Varitems['EntryVar']),3):
            tmp.remove(i)
            try:
                if float(self.Varitems['EntryVar'][i].get()) <= 0 or float(self.Varitems['EntryVar'][i].get()) > 1:
                    msg.showerror(self.lang.error, self.lang.probabilityerror)
                    return 0
            except:
                msg.showerror(self.lang.error, self.lang.probabilityerror)
                return 0
            
        for i in tmp:
            try:
                if float(self.Varitems['EntryVar'][i].get()) < 0:
                    msg.showerror(self.lang.error, self.lang.mgerror)
                    return 0
            except:
                msg.showerror(self.lang.error, self.lang.mgerror)
                return 0          
        
        tmp = 0;n = 1
        for i in self.database['data']:
            n += 1
            for j in self.database['data'][i]:
                tmp += 1
                self.data[self.CurrentData]['data'][i][j] = self.Varitems['EntryVar'][tmp - 1].get()
                if j == 'SMG':
                    if not self.Varitems['CheckboxVar'][int(tmp - n)].get():
                        self.data[self.CurrentData]['data'][i]['SMG'] = '0'
                        continue
                if j == 'BMG':
                    if not self.Varitems['CheckboxVar'][int(tmp - n)].get():
                        self.data[self.CurrentData]['data'][i]['BMG'] = '0'
                        continue
            
        with open('.\\database.json', 'w+', encoding='utf-8') as file:
            file.write(json.dumps(self.data, ensure_ascii=False, indent=4))
        self.Reload()
    @TestFun
    def setDB(self,database):
        self.CurrentData = database
        self.database = self.data.get(database)
        self.Reload()
    @TestFun
    def delDB(self):
        if self.isdeldb == 1:
            return 0
        self.isdeldb = 1
        n = msg.askokcancel(title=self.lang.deletedb, message=self.lang.deletedbmsg)
        if n:
            if self.CurrentData == 'default':
                msg.showerror(self.lang.error, self.lang.nodbdel)
                self.isdeldb = 0
                return 0
            tmp = {}
            for i in self.data:
                if i == self.CurrentData:
                    continue
                else:
                    tmp[i] = self.data[i]
            self.data = tmp
            self.database = tmp['default']
            self.CurrentData = 'default'
            self.Reload()
            self.SaveChange()
        self.isdeldb = 0
    @TestFun
    def ChangeItemData(self):
        try:
            if not self.ChangeItemDataWindow.isopen:
                self.ChangeItemDataWindow = ItemDataSettings_UI(TopLevel= self.tk, data=self.CurrentData)
                self.ChangeItemDataWindow.PrepareUILoading()
                self.tk.after(10,self._ChangeItemData)
        except AttributeError:
            self.ChangeItemDataWindow = ItemDataSettings_UI(TopLevel= self.tk, data=self.CurrentData)
            self.ChangeItemDataWindow.PrepareUILoading()
            self.tk.after(10,self._ChangeItemData)
        except:
            pass

    def _ChangeItemData(self):
        if self.ChangeItemDataWindow.ReturnData != '' and self.ChangeItemDataWindow.ReturnData != '0':
            self.Loadjson()
            self.Reload()
            self.SaveChange()
        elif self.ChangeItemDataWindow.ReturnData == '0':
            pass
        else:
            self.tk.after(10,self._ChangeItemData)
    @TestFun
    def newDB(self):
        try:
            if not self.CreateNewDBWindow.isopen:
                self.CreateNewDBWindow = CreateNewWindow(self.tk, self.lang.newdb)
                self.CreateNewDBWindow.PrepareUILoading()
                self.tk.after(10,self._newDB)
        except AttributeError:
            self.CreateNewDBWindow = CreateNewWindow(self.tk, self.lang.newdb)
            self.CreateNewDBWindow.PrepareUILoading()
            self.tk.after(10,self._newDB)

        except:
            pass
    
    def _newDB(self):
        if self.CreateNewDBWindow.ReturnData != '' and self.CreateNewDBWindow.ReturnData != '0':
            if self.CreateNewDBWindow.ReturnData in list(self.data.keys()):
                msg.showerror(self.lang.error,self.lang.notsamenameerror)
                return 0
            self.data[self.CreateNewDBWindow.ReturnData] = {'sample':{'BMG':[], 'main':[]}, 'data':{'sample':{'probability':'1','SMG':'0', 'BMG':'0'}}}
            self.Reload()
            self.SaveChange()
        elif self.CreateNewDBWindow.ReturnData == '0':
            pass
        else:
            self.tk.after(10,self._newDB)
    @TestFun
    def setLanguage(self,language):
        n = msg.askokcancel(self.lang.chooselang, self.lang.chooselangmsg)
        if n:
            with open('.\\language', 'w') as l:
                l.write(language)
            sys.exit()
    @TestFun
    def CreateNew(self):
        tmp = {}
        tmp1 = {}
        try:
            if not self.CreateNewItemWindow.isopen:
                self.CreateNewItemWindow = CreateNewWindow(self.tk, self.lang.newitem)
                self.CreateNewItemWindow.PrepareUILoading()
                self.tk.after(10,self._CreateNew,tmp,tmp1)
        except AttributeError:
            self.CreateNewItemWindow = CreateNewWindow(self.tk, self.lang.newitem)
            self.CreateNewItemWindow.PrepareUILoading()
            self.tk.after(10,self._CreateNew,tmp,tmp1)
        except:
            pass

    def _CreateNew(self,tmp,tmp1):
        if self.CreateNewItemWindow.ReturnData != '' and self.CreateNewItemWindow.ReturnData != '0':
            if self.CreateNewItemWindow.ReturnData in list(self.database.keys()):
                msg.showerror(self.lang.error,self.lang.notsamenameerror)
                return 0
            for i in self.data[self.CurrentData]:
                if i == 'data':
                    continue
                tmp1[i] = self.data[self.CurrentData][i]
            tmp1[self.CreateNewItemWindow.ReturnData] = {'BMG':['sample'], 'main':['sample'] }
            for i in self.data[self.CurrentData]['data']:
                tmp[i] = self.data[self.CurrentData]['data'][i]
            tmp[self.CreateNewItemWindow.ReturnData] = {'probability': '1', 'SMG': '0', 'BMG': '0'}
            tmp1['data'] = tmp
            tmp = {}
            for i in self.data:
                if i == self.CurrentData:
                    tmp[i] = tmp1
                else:
                    tmp[i] = self.data[i]
            self.data = tmp
            self.database = tmp1
            self.Reload()
            self.SaveChange()
        elif self.CreateNewItemWindow.ReturnData == '0':
            pass
        else:
            self.tk.after(10,self._CreateNew,tmp,tmp1)
    @TestFun
    def Del(self, data):
        if self.isdel == 1:
            return 0
        self.isdel = 1
        n = msg.askokcancel(title=self.lang.deleteitem, message=self.lang.deleteitemmsg)
        if n and len(self.data[self.CurrentData]['data']) > 1:
            tmp = {}
            tmp1 = {}
            for i in self.data[self.CurrentData]:
                if i == data or i == 'data':
                    continue
                else:
                    tmp1[i] = self.data[self.CurrentData][i]
            for i in self.data[self.CurrentData]['data']:
                if i == data:
                       pass
                else:
                    tmp[i] = self.data[self.CurrentData]['data'][i]
            tmp1['data'] = tmp
            tmp = {}
            for i in self.data:
                if i == self.CurrentData:
                    tmp[i] = tmp1
                else:
                    tmp[i] = self.data[i]
            self.data = tmp
            self.database = tmp1
            self.Reload()
            self.SaveChange()
        elif n and len(self.data[self.CurrentData]['data']) <= 1:
            msg.showerror(self.lang.option,self.lang.optionmsg)
        self.isdel = 0
    @TestFun
    def Rename(self, data):
        try:
            if not self.RenameWindow.isopen:
                tmp = {}
                tmp1 = {}
                self.RenameWindow = CreateNewWindow(self.tk, self.lang.rename,data)
                self.RenameWindow.PrepareUILoading()
                self.tk.after(10,self._Rename,data,tmp,tmp1)
        except AttributeError:
            tmp = {}
            tmp1 = {}
            self.RenameWindow = CreateNewWindow(self.tk, self.lang.rename,data)
            self.RenameWindow.PrepareUILoading()
            self.tk.after(10,self._Rename,data,tmp,tmp1)
        except:
            pass  
        
    def _Rename(self, data,tmp,tmp1):
        if self.RenameWindow.ReturnData != '' and self.RenameWindow.ReturnData != '0':
            if self.RenameWindow.ReturnData in list(self.database.keys()):
                msg.showerror(self.lang.error,self.lang.notsamenameerror)
                return 0
            for i in self.data[self.CurrentData]:
                if i == data:
                    tmp1[self.RenameWindow.ReturnData] = self.data[self.CurrentData][i]
                elif i == 'data':
                    continue
                else:
                    tmp1[i] = self.data[self.CurrentData][i]
            for i in self.data[self.CurrentData]['data']:
                if i == data:
                    tmp[self.RenameWindow.ReturnData] = self.data[self.CurrentData]['data'][i]
                else:
                    tmp[i] = self.data[self.CurrentData]['data'][i]
            tmp1['data'] = tmp
            tmp = {}
            for i in self.data:
                if i == self.CurrentData:
                    tmp[i] = tmp1
                else:
                    tmp[i] = self.data[i]
            self.data = tmp
            self.database = tmp1
            self.RenameWindow.ReturnData = ''
            self.SaveChange()
        elif self.RenameWindow.ReturnData == '0':
            pass
        else:
            self.tk.after(10,self._Rename,data,tmp,tmp1)
    @TestFun
    def About(self):
        if self.about_isopen == 1:
            return 0
        self.about_isopen = 1
        msg.showinfo(self.lang.about,self.lang.aboutmsg)
        self.about_isopen = 0

    def TextLoading(self):
        for i in range(len(self.database['data'])):
            self.items['Text'].append(tk.Label(self.tk, text=list(self.database['data'].keys())[i] + ' ' + self.lang.probability))
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
            self.Varitems['EntryVar'][-1].set(str(self.database['data'][i]['probability']))
            self.Varitems['EntryVar'].append(tk.StringVar())
            self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=5))
            self.items['Entry'][-1].grid(row=tmp, column=3, padx=5)
            self.Varitems['EntryVar'][-1].set(str(self.database['data'][i]['SMG']))
            self.Varitems['EntryVar'].append(tk.StringVar())
            self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=5))
            self.items['Entry'][-1].grid(row=tmp, column=5, padx=10)
            self.Varitems['EntryVar'][-1].set(str(self.database['data'][i]['BMG']))
            self.Varitems['CheckboxVar'].append(tk.IntVar())
            self.items['Checkbox'].append(ttk.Checkbutton(self.tk, text=self.lang.smg, variable=self.Varitems['CheckboxVar'][-1]))
            self.items['Checkbox'][-1].grid(row=tmp, column=2, padx=10)
            self.Varitems['CheckboxVar'][-1].set(bool(self.database['data'][i]['SMG'] != '0'))
            self.Varitems['CheckboxVar'].append(tk.IntVar())
            self.items['Checkbox'].append(ttk.Checkbutton(self.tk, text=self.lang.bmg, variable=self.Varitems['CheckboxVar'][-1]))
            self.items['Checkbox'][-1].grid(row=tmp, column=4, padx=10)
            self.Varitems['CheckboxVar'][-1].set(bool(self.database['data'][i]['BMG'] != '0'))
            tmp += 1
        self.finalcloumn = tmp
        
    def ButtonLoading(self):
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.setitemdata, width=25, command=self.ChangeItemData))
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
        if self.CurrentData == 'default':
            self.items['Button'][2].configure(state = 'disabled')
        else:
            self.items['Button'][2].configure(state = 'normal')

class CreateNewWindow(_UI):

    def __init__(self, TopLevel = False, title = 'New', varset = ''):
        super().__init__(TopLevel)
        self.tk.title(title)
        self.varset = varset
        self.ReturnData = ''
    
    def Save(self):
        if self.Varitems['TextVar'][-1].get():
            self.ReturnData = self.Varitems['TextVar'][-1].get()
            self._close()
        else:
            msg.showerror(self.lang.error, self.lang.inputname)
        
    
    def Cancel(self):
        self.ReturnData = '0'
        self._close()

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
        self._close()
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
            self.label.after(9, self.update_frame)
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
        super().__init__(TopLevel, dataload = data)

        self.tk.title(self.lang.setitemdata)
        self.ReturnData = ''
    
    def Save(self):
        tmp = 0
        for i in self.database:
            if i != 'data':
                for j in self.database[i]:
                    self.data[self.CurrentData][i][j] = eval('[' + self.Varitems['EntryVar'][tmp].get() + ']')
                    tmp += 1
        
        with open('.\\database.json', 'w+', encoding='utf-8') as file:
            file.write(json.dumps(self.data, ensure_ascii=False, indent=4))
        self.ReturnData = '1'
        self._close()
    
    def Cancel(self):
        self.ReturnData = '0'
        self._close()

    def TextLoading(self):
        tmp = 0
        for i in self.database:
            if i != 'data':
                for j in self.database[i]:
                    if j == 'main':
                        self.items['Text'].append(tk.Label(self.tk, text= i + ' ' + self.lang.res + ':'))
                    else:
                        self.items['Text'].append(tk.Label(self.tk, text= i + ' ' + self.lang.bmg + ':'))
                    self.items['Text'][-1].grid(row=tmp, column=0, padx=5, pady=5)
                    tmp += 1
    
    def InputLoading(self):
        tmp = 0
        for i in self.database:
            if i != 'data':
                for j in self.database[i]:
                    self.Varitems['EntryVar'].append(tk.StringVar())
                    self.items['Entry'].append(ttk.Entry(self.tk, textvariable=self.Varitems['EntryVar'][-1], width=80))
                    self.items['Entry'][-1].grid(row=tmp, column=1, padx=10)
                    self.Varitems['EntryVar'][-1].set(str(self.database[i][j])[1:-1])
                    tmp += 1
        self.finalcolumn = tmp
    
    def ButtonLoading(self):
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.save, width=80, command=self.Save))
        self.items['Button'][-1].grid(row=self.finalcolumn + 1, column=0, columnspan=2, padx=20, pady=10)
        self.items['Button'].append(ttk.Button(self.tk, text=self.lang.cancel, width=80, command=self.Cancel))
        self.items['Button'][-1].grid(row=self.finalcolumn + 2, column=0, columnspan=2, padx=20, pady=10)