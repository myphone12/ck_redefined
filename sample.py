import tkinter as tk
 
def handle_menu_item(menu_item_data):
    print("你选择了:", menu_item_data)
 
root = tk.Tk()
 
menu_data = ["选项1", "选项2", "选项3"]
 
menu = tk.Menu(root)
for item in menu_data:
    menu.add_command(label=item, command=lambda data=item: handle_menu_item(data))
 
root.config(menu=menu)
 
root.mainloop()