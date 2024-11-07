import tkinter as tk
from tkinter import ttk, messagebox as msg

from reck import Ck

class main_UI:

    def __init__(self, set = 'default'):
        self.ck = Ck(set)
        self.tk = tk.Tk()
        self.tk.iconbitmap('.\\icon.ico')
        self.tk.title('Wish stimulator')
        self.tk.resizable(0,0)

        self.WishDataVar = tk.StringVar()
        self.WishData = ''
    
    def OneWish(self):
        self.WishData += str(self.ck.ck(ReturnLevel = 1)[0])
        self.WishDataVar.set(self.WishData)
    
    def TenWish(self):
        self.WishData += str(self.ck.ck(cishu= 10, ReturnLevel = 1))
        self.WishDataVar.set(self.WishData)
    
    def MenuLoading(self):
        pass
    
    def ButtonLoading(self):
        self.wish_button1 = ttk.Button(self.tk, text='One wish', width=10, command=self.OneWish)
        self.wish_button1.grid(row=2, column=1, padx=20, pady=10)
        self.wish_button2 = ttk.Button(self.tk, text='Ten wish', width=10, command=self.TenWish)
        self.wish_button2.grid(row=2, column=2, padx=20, pady=10)

    def TextLoading(self):
        self.wish_text1 = tk.Label(self.tk, textvariable = self.WishDataVar, anchor='n', 
                           font=("Microsoft Yahei UI", 9),fg='orange')
        self.wish_text1.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

    def PrepareUILoading(self):
        self.ButtonLoading()
        self.TextLoading()
        self.tk.mainloop()