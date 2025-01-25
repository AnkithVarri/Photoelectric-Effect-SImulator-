import tkinter as tk
import time

def reset_timer(event=None):
    activity_time = time.time()
    return activity_time

def check_inactivity():
    if reset_timer() - last_activity_time > timeout:
        print("Inactivity detected!")
        root.destroy()
    else:
        root.after(1000, check_inactivity)

timeout = 5  # In seconds
last_activity_time = time.time()

root = tk.Tk()
root.geometry("300x200")

# Bind activity events
root.bind_all("<Key>", reset_timer)
root.bind_all("<Motion>", reset_timer)
root.bind_all("<Button>", reset_timer)

# Start inactivity check
while True:
    check_inactivity()
    root.mainloop()