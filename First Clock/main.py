from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
intervals = 4  # Default intervals
check_marks = ""
timer_id = None


# ---------------------------- Customize Timer ------------------------------- #
def update_work_min(event):
    global WORK_MIN
    WORK_MIN = int(enter_timer.get())
    enter_timer.config(bg=GREEN)
    print(f"Updated Work Time: {WORK_MIN} minutes")


def update_short_break(event):
    global SHORT_BREAK_MIN
    SHORT_BREAK_MIN = int(enter_short_break.get())
    enter_short_break.config(bg=GREEN)
    print(f"Updated Short Break Time: {SHORT_BREAK_MIN} minutes")


def update_long_break(event):
    global LONG_BREAK_MIN
    LONG_BREAK_MIN = int(enter_long_break.get())
    enter_long_break.config(bg=GREEN)
    print(f"Updated Long Break Time: {LONG_BREAK_MIN} minutes")


def update_intervals(event):
    global intervals
    intervals = int(enter_interval.get())
    enter_interval.config(bg=GREEN)
    print(f"Updated Total Intervals: {intervals}")


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, check_marks, timer_id
    reps = 0
    check_marks = ""
    if timer_id:
        window.after_cancel(timer_id)
    canvas.itemconfig(timer, text="00:00")
    Label.config(title_label, text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    check_mark_label.config(text=check_marks)


def reset_to_default():
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, intervals
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    intervals = 4

    # Reset entry fields
    entries = [enter_timer, enter_short_break, enter_long_break, enter_interval]
    for entry in entries:
        entry.delete(0, END)
        entry.insert(END, "Enter No")
        entry.config(bg="white")  # Reset background color to default

    reset_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps, check_marks, timer_id

    if reps < intervals * 2:
        if reps % 2 == 0:
            count_down(WORK_MIN * 60)
            Label.config(title_label, text="Work Time", fg=GREEN, font=(FONT_NAME, 35, "bold"))
        else:
            if reps == intervals * 2 - 1:
                count_down(LONG_BREAK_MIN * 60)
                Label.config(title_label, text="Long Break", fg=RED, font=(FONT_NAME, 35, "bold"))
            else:
                count_down(SHORT_BREAK_MIN * 60)
                Label.config(title_label, text="Short Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
        reps += 1
        if reps % 2 == 0:
            check_marks += "✔"
            check_mark_label.config(text=check_marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer_id
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_id = window.after(1000, count_down, count - 1)
    else:
        start_count()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Timer")

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=350, height=300, highlightthickness=0)
img = PhotoImage(file="tomato.png")
a = canvas.create_image(180, 120, image=img)
timer = canvas.create_text(180, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

intro_label = Label(text="This is a Pomodoro Timer. It helps you work better by breaking your time into small chunks. "
                         "You can divide 100 min work into 4 intervals of 25 minutes, then take a short 5-minute "
                         "break. After working for 100 minutes, you can take a longer 20-minute break. It helps you "
                         "stay focused and feel less tired. Click start button on left to proceed",
                    wraplength=250)
intro_label.grid(column=2, row=1, padx=5, pady=5)

start_button = Button(text="Start", command=start_count)
reset_button = Button(text="Reset", command=reset_timer)
reset_default_button = Button(text="Reset to Default", command=reset_to_default)
start_button.grid(column=0, row=2, padx=20, pady=20, sticky="ew")
reset_button.grid(column=2, row=2, padx=20, pady=20, sticky="ew")
reset_default_button.grid(column=1, row=7, padx=20, pady=20, sticky="ew")

customize_label = Label(text="Customize the timer by changing timer components: ")
customize_label.grid(column=1, row=3)

timer_label = Label(text="Enter Work/Study Time (min)")
timer_label.grid(column=2, row=3, padx=5, pady=5)

enter_timer = Entry(width=6)
enter_timer.insert(END, string="Enter No")
enter_timer.grid(column=3, row=3, padx=5, pady=5)
enter_timer.bind("<Return>", update_work_min)

short_break_label = Label(text="Enter Short Break Time (min)")
short_break_label.grid(column=2, row=4)

enter_short_break = Entry(width=6)
enter_short_break.insert(END, string="Enter No")
enter_short_break.grid(column=3, row=4, padx=5, pady=5)
enter_short_break.bind("<Return>", update_short_break)

long_break_label = Label(text="Enter Long Break Time (min)")
long_break_label.grid(column=2, row=5)

enter_long_break = Entry(width=6)
enter_long_break.insert(END, string="Enter No")
enter_long_break.grid(column=3, row=5, padx=5, pady=5)
enter_long_break.bind("<Return>", update_long_break)

interval_label = Label(text="Total Intervals")
interval_label.grid(column=2, row=6)

enter_interval = Entry(width=6)
enter_interval.insert(END, string="Enter No")
enter_interval.grid(column=3, row=6, padx=5, pady=5)
enter_interval.bind("<Return>", update_intervals)

check_mark_label = Label(text=check_marks, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(column=1, row=2)




window.mainloop()
