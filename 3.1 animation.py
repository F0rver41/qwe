import tkinter as tk
import math
import time


def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    canvas.delete("all")

    canvas.create_oval(50, 50, 250, 250, width=2)

    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = 150 + 80 * math.cos(angle)
        y = 150 + 80 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=('Arial', 12))

    hour_angle = math.radians(hours * 30 + minutes * 0.5 - 90)
    minute_angle = math.radians(minutes * 6 - 90)
    second_angle = math.radians(seconds * 6 - 90)

    hour_x = 150 + 40 * math.cos(hour_angle)
    hour_y = 150 + 40 * math.sin(hour_angle)
    canvas.create_line(150, 150, hour_x, hour_y, width=4, fill='black')

    minute_x = 150 + 60 * math.cos(minute_angle)
    minute_y = 150 + 60 * math.sin(minute_angle)
    canvas.create_line(150, 150, minute_x, minute_y, width=3, fill='blue')

    second_x = 150 + 70 * math.cos(second_angle)
    second_y = 150 + 70 * math.sin(second_angle)
    canvas.create_line(150, 150, second_x, second_y, width=1, fill='red')

    root.after(1000, update_clock)

root = tk.Tk()
root.title("Простые часы")

canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()

update_clock()

root.mainloop()