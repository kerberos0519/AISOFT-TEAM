import tkinter as tk
import time
from tkcalender import Calendar, DateEntry

# GUI 창 생성
root = tk.Tk()
root.title("Timer")



# 사용자로부터 타이머 시간 입력받기
def get_timer():
    timer_input = f"{cal.selection_get()} {hour_entry.get()}:{minute_entry.get()}:{second_entry.get()}"
    timer(timer_input)

# 타이머 함수 정의
def timer(timer_input):
    target_time = time.strptime(timer_input, "%Y-%m-%d %H:%M:%S")
    target_timestamp = time.mktime(target_time)

    while True:
        current_timestamp = time.time()
        remaining_time = target_timestamp - current_timestamp

        if remaining_time < 0:
            label.config(text="Time's up!")
            break

        remaining_time = int(remaining_time)

        days, remaining_time = divmod(remaining_time, 86400)
        hours, remaining_time = divmod(remaining_time, 3600)
        mins, secs = divmod(remaining_time, 60)

        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(
            days, hours, mins, secs)
        label.config(text=timer)
        root.update()
        time.sleep(1)

# 년, 월, 일 선택 창 생성
cal = Calendar(root, font=("Helvetica", 15))
cal.pack(pady=10)

# 시간 입력 창 생성
hour_label = tk.Label(root, text="시", font=("Helvetica", 16))
hour_label.pack(side="left", padx=5)

hour_entry = tk.Entry(root, font=("Helvetica", 24))
hour_entry.pack(side="left", padx=5)
hour_entry.insert(0, "00")

minute_label = tk.Label(root, text="분", font=("Helvetica", 16))
minute_label.pack(side="left", padx=5)

minute_entry = tk.Entry(root, font=("Helvetica", 24))
minute_entry.pack(side="left", padx=5)
minute_entry.insert(0, "00")

second_label = tk.Label(root, text="초", font=("Helvetica", 16))
second_label.pack(side="left", padx=5)

second_entry = tk.Entry(root, font=("Helvetica", 24))
second_entry.pack(side="left", padx=5)
second_entry.insert(0, "00")

# 타이머 시작 버튼 생성
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=get_timer)
start_button.pack(side="left", padx=5)

stop_button = tk.Button(button_frame, text="Stop", command=root.destroy)
stop_button.pack(side="left", padx=5)

# 타이머 라벨 생성
label = tk.Label(root, text="00:00:00:00:00:00", font=("Helvetica", 48))
label.pack(pady=10)

root.mainloop()
