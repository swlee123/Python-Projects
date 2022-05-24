import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    global work
    reps = 0
    work = 0
    check_mark.config(text="✅" * work)
    label_1.config(text="Timer", fg="Cyan")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global work
    reps += 1
    work_sec = WORK_MIN*60
    break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        countdown(long_break_sec)
        label_1.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        work += 1
        check_mark.config(text="✅" * work)
        countdown(break_sec)
        label_1.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        label_1.config(text="Work",  fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):

    minute = int(time / 60)
    sec = time % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if time > 0:
        global timer
        timer = window.after(1000, countdown, time-1)
    elif time == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)





label_1 = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg="Cyan")
label_1.grid(column=1, row=0)

start_button = tk.Button(text="Start", font=(FONT_NAME, 10, "normal"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 10, "normal"),command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = tk.Label(text="✅"*work, fg=GREEN, font=(FONT_NAME, 10, "normal"),bg=YELLOW,highlightthickness=0)
check_mark.grid(column=1, row=2)



window.mainloop()


