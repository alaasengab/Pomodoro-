from tkinter import * 
import math 
#------------------------------Pomodoro Technique------------------------
"""Here's a basic description:

Set a Timer: Choose a specific time interval, typically 25 minutes, to work on a task without distractions.
Work Focused: Set your timer and work on your chosen task without interruptions.
Take a Break: Once the timer goes off, take a short break of 5-10 minutes.
Repeat: After completing four Pomodoro intervals, take a longer break of 15-30 minutes.

"""
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
timer = NONE
# ---------------------------- CountDown MECHANISM ------------------------------- #


# reset button that will stop the timer, reset the timer to 00:00 and reset checkmarks 
def reset_all ():
    #stop the timer 
    window.after_cancel(timer)
    #reset timer label to read timer 
    title_label["text"] = "Timer" 
    #reset timer to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #reset check marks 
    check_marks.config(text="")
    global reps 
    reps = 0 
    
    


# start timer once start button is clicked
def start_timer():
    global reps
    reps += 1 
    count_down(30*60)
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=PINK) 
    elif reps % 2 == 0: 
        count_down(short_break_sec)
        title_label.config(text="Break",fg=GREEN) 
    else: 
        count_down(work_sec)
        title_label.config(text="WORK", fg=RED)
        


# function to proceed with count down 
def count_down(count):
    count_min = math.floor( count / 60 )
    count_sec = round(count % 60, 3)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else: 
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        check_marks.config(text=marks)
        

# ---------------------------- UI Setup ------------------------------- #

window= Tk()
window.title ("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#top label 
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
title_label.grid(column=1,row=0)
# inset pic 
canvas = Canvas(width=200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text= canvas.create_text(100,130, text= "00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#Buttons 
#start 
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0,row=2)
#Reset 
Reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_all)
Reset_button.grid(column=3, row=2)

#CheckMarks 
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()
