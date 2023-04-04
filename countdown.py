import datetime
import tkinter as tk
from PIL import Image, ImageTk

# tkinter 윈도우 생성
window = tk.Tk()
window.geometry("400x400")
window.title("2023 정보처리기사 1회 실기시험 남은 시간")

# 이미지 불러오기
img = Image.open("1.png")
img = img.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

# 이미지 레이블 생성
image_label = tk.Label(window, image=photo)
image_label.pack(pady=20)

# 라벨 생성
label = tk.Label(window, text="시험날짜를 입력하세요. (yyyy-mm-dd):", font=("Arial", 16))
label.pack(pady=20)

# 입력받는 텍스트 박스 생성
input_box = tk.Entry(window, font=("Arial", 16))
input_box.pack()

# 일, 시, 분, 초를 출력하는 라벨 생성
time_label = tk.Label(window, text="", font=("Arial", 20, "bold"))
time_label.pack()

# 남은 시간을 계산하는 함수
def get_remaining_time():
    # 현재 날짜와 시간 가져오기
    now = datetime.datetime.now()

    # 입력받은 목표 날짜 가져오기
    try:
        target_date = datetime.datetime.strptime(input_box.get(), "%Y-%m-%d")
    except ValueError:
        time_label.config(text="올바른 날짜 형식이 아닙니다.")
        return

    # 입력받은 목표 날짜와 현재 날짜와의 차이 계산
    remaining_time = target_date - now
    if remaining_time.days < 0:
        time_label.config(text="목표 날짜가 이미 지났습니다.")
        return
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds
    
# 윈도우 업데이트 함수
def update():
    remaining_time = get_remaining_time()
    if remaining_time:
        time_str = f"{remaining_time[0]}일 {remaining_time[1]:02d}시간 {remaining_time[2]:02d}분 {remaining_time[3]:02d}초"
        time_label.config(text=time_str)
    window.after(1000, update)

# 윈도우 업데이트 시작
update()

# tkinter 윈도우 실행
window.mainloop()