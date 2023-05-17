import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title("Fair Play")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Info")
user_info_frame.grid(row=0, column=0)

first_name_label = tkinter.Label(user_info_frame, text="First Name: ")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name: ")
last_name_label.grid(row=1, column=0)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

button = tkinter.Button(frame, text="Enter data")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()