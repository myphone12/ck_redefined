import cv2  # 导入 OpenCV 库
from PIL import Image, ImageTk  # 导入 PIL 库以处理图像
import tkinter as tk  # 导入 tkinter 库
from tkinter import ttk  # 导入ttk模块以获取美观的部件

# 创建一个主窗口
root = tk.Tk()
root.title("视频播放器")  # 设置窗口标题
root.geometry("800x600")  # 设置窗口大小
# 定义播放视频的函数
def play_video():
    # 打开视频文件
    cap = cv2.VideoCapture(".\\sddl.mp4")
    
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("无法打开视频文件")
        return

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk  
            label.configure(image=imgtk)
            label.after(20, update_frame)
        else:
            cap.release()
    label = ttk.Label(root)
    label.pack(padx=10, pady=10)
    update_frame()
root.mainloop()