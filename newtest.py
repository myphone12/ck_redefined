import tkinter as tk

def ppp():
    return 111111111
def ddd():
    print(root.after(10,ppp))
root = tk.Tk()
a = tk.Frame(root,width=100,height=100)
a.place(x=0,y=0)
b = tk.Button(a,text='111',command=ddd,width=90,height=90)
b.pack()
root.mainloop()