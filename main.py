import tkinter as tk
from tkinter import ttk

root = tk.Tk() # instantiate an instance of a window
root.geometry('1000x1000')
root.title('Workout App')

#icon = PhotoImage() ##changes icon in top corner

seconds = 0
minutes = 00
hours = 00
running = False

exercises = ['Select an Exercise', 'Squat', 'Bench', 'Deadlift']

def update_timer():
    global seconds
    global minutes
    global hours
    if running:
        seconds += 1
        if seconds >= 60:
            minutes += 1
            seconds -= 60
        if minutes >= 60:
            hours += 1
            minutes -= 60
        time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)  # call again in 1 second

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    global seconds
    global minutes
    global hours
    global running
    running = False
    seconds = 0
    minutes = 0
    hours = 0

def select_exercise(event):
    selection = combo.get()
    exercise_label = tk.Label(label_frame, text = selection)
    exercise_label.pack()
    combo.pack_forget()

def add_exercise():
    global combo
    combo = ttk.Combobox(root, values=exercises, state="readonly")
    combo.current(0)
    combo.pack(pady=10)
    combo.bind("<<ComboboxSelected>>", select_exercise)

def start_workout():
    start_workout_btn.pack_forget()
    end_workout_btn.pack()
    add_exercise_btn.pack()
    time_label.pack()
    start_timer()

def end_workout():
    stop_timer()
    start_workout_btn.pack()
    add_exercise_btn.pack_forget()
    end_workout_btn.pack_forget()
    time_label.pack_forget()    


frame = tk.Frame(root)
frame.config(width=500, height=500, borderwidth=2, relief='sunken')
frame.pack()

label_frame = tk.Frame(root)
label_frame.pack()

time_label = tk.Label(frame)

exercise_label = tk.Label(frame, text = 'Select an Exercise')

add_exercise_btn = tk.Button(frame, text = 'Add exercise', command = add_exercise)


start_workout_btn = tk.Button(frame, text="Start Workout", command=start_workout)
start_workout_btn.pack()

end_workout_btn = tk.Button(frame, text= "End workout", command=end_workout)


root.mainloop() # places window in computer screen