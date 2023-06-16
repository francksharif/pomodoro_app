from tkinter import *

window = Tk()
window.title("Pomodoro App")
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1500)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = int(count / 60)
    count_secondes = count % 60
    if count_secondes < 10:
        count_secondes = f"0{count_secondes}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_secondes}")
    if count > 0:
        window.after(1000,count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window.config(padx=100, pady=50, bg=YELLOW)
#Image and timer setup
canvas = Canvas(width=220, height=274, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100,112, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

#Buttons and labels setup
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)
valid_pomodoro = Label(text="✅")
start_button = Button(text="Start", bg="white", pady=5, padx=15, font=("bold"), command=start_timer)
reset_button = Button(text="Reset", bg="white", pady=5, padx=15, font=("bold"))
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
valid_pomodoro.grid(column=1, row=3)


window.mainloop()


#Test

