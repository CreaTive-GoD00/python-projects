from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BG = "#FDF4AF"
BUTTON_BG = "#A5E9DD"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer_job = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    global timer_job

    if timer_job is not None:
        window.after_cancel(timer_job)
        timer_job = None

    reps = 0

    timer.config(text="Timer", fg="#34908B")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (1, 3, 5, 7):
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)

    elif reps in (2, 4, 6):
        timer.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)

    elif reps == 8:
        timer.config(text="Long Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer_job
    global reps

    count_mins = math.floor(count / 60)
    count_secs = count % 60

    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(
        timer_text,
        text=f"{count_mins}:{count_secs}"
    )

    if count > 0:
        timer_job = window.after(
            1000,
            count_down,
            count - 1
        )

    else:
        work_sessions = math.floor((reps + 1) / 2)

        marks = ""
        for _ in range(work_sessions):
            marks += "✔"

        checkmarks.config(text=marks)

        if reps == 8:
            reps = 0

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(
    bg=BG,
    pady=50,
    padx=100
)

canvas = Canvas(
    width=200,
    height=224,
    bg=BG,
    highlightthickness=0
)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(
    100,
    112,
    image=tomato_img
)

timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 24, "bold")
)

canvas.grid(column=1, row=1)

timer = Label(
    text="Timer",
    font=(FONT_NAME, 35, "bold"),
    fg="#34908B",
    bg=BG,
    highlightthickness=0
)

timer.grid(column=1, row=0)

start_button = Button(
    text="Start",
    bg=BUTTON_BG,
    fg="#34908B",
    font=(FONT_NAME, 18, "bold"),
    highlightthickness=0,
    command=start_timer
)

start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    bg=BUTTON_BG,
    fg="#34908B",
    font=(FONT_NAME, 18, "bold"),
    highlightthickness=0,
    command=reset
)

reset_button.grid(column=2, row=2)

checkmarks = Label(
    text="",
    font=(FONT_NAME, 20, "bold"),
    fg="green",
    bg=BG,
    highlightthickness=0
)

checkmarks.grid(column=1, row=3)

window.mainloop()