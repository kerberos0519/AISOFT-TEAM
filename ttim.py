import datetime
import tkinter as tk
from tkcalendar import DateEntry
from babel.numbers import*

# GUI 생성
root = tk.Tk()
root.geometry("1400x1000")
root.title("남은시간 계산기")

# 날짜 선택 위젯
date_label = tk.Label(root, text="목표 날짜:", font=("Helvetica", 18))
date_label.grid(row=0, column=0)

date_entry = DateEntry(root, width=12, font=("Helvetica", 18))
date_entry.grid(row=0, column=1)

# 남은 시간 출력 레이블
remaining_time_label = tk.Label(root, text="남은 시간:", font=("Helvetica", 18),fg="red")
remaining_time_label.grid(row=1, column=0)

remaining_time_var = tk.StringVar()
remaining_time_var.set("")
remaining_time_text = tk.Label(root, textvariable=remaining_time_var, font=("Helvetica", 18))
remaining_time_text.grid(row=1, column=1)

# 시간 업데이트 함수
def update_time():
    # 목표 시간 계산
    goal_date = date_entry.get_date()
    goal_time = datetime.datetime.combine(goal_date, datetime.time())
    
    # 남은 시간 업데이트
    remaining_time = goal_time - datetime.datetime.now()
    remaining_time_str = str(remaining_time).split(".")[0]
    remaining_time_var.set(remaining_time_str)
    
    # 1초마다 업데이트
    root.after(1000, update_time)

# 이미지 로드
img = tk.PhotoImage(file="jan.gif")

# 이미지 표시
img_label = tk.Label(root, image=img)
img_label.grid(row=2, column=0, columnspan=2)


# 시간 업데이트 함수 실행
update_time()

# GUI 실행
root.mainloop()

print("하이")