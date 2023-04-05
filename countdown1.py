from tkinter import *
from PIL import Image, ImageTk

import time

root = Tk()
root.title("냐밍")
root.geometry("750x450")
root.configure(bg="black")





def countdown():
    event = "2023-05-25 12:40:00"
    event_time = time.strptime(event, "%Y-%m-%d %H:%M:%S")
    current_time = time.localtime()
    seconds_left = int(time.mktime(event_time) - time.mktime(current_time))
    days = seconds_left // 86400
    hours = (seconds_left - days * 86400) // 3600
    minutes = (seconds_left - days * 86400 - hours * 3600) // 60
    seconds = seconds_left - days * 86400 - hours * 3600 - minutes * 60
    time_left = f"합격까지 {days}일 {hours} : {minutes}: {seconds} 남았습니다.(람쥐)"
    time.label.config(text=time_left)

    root.after(1000, countdown)
    


time.label = Label(root, font=("Computer Modern Roman", 25), fg="green", bg="yellow")
time.label.pack(pady=20)

#gif 실행 파일
frameCnt = 20
frames = [PhotoImage(file="C:\\Users\\user\\Pictures\\Screenshots\\ezgif.com-rotate.gif", format='gif -index %i' % (i)) for i in range(frameCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    
    Image.label.configure(image=frame)
    root.after(100, update, ind)

Image.label = Label(root)
Image.label.pack()
root.after(0, update, 0)

countdown()

root.mainloop()