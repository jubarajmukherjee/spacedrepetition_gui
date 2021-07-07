# import tkinter and all its functions
from tkinter import *

root = Tk() # create root window
root.title("Spaced Repetition")
root.config(bg="skyblue")




left_frame = Frame(root, width=250, height=340)
left_frame.grid(row=0, column=0, padx=10, pady=10)

subject = Label(left_frame, text="Enter the Subject studied:").grid(row=0,column=0)
subject_box = Entry(left_frame)
subject_box.grid(row=0,column=1)

date = Label(left_frame, text="Enter the DATE studied on:").grid(row=1,column=0)
date_box=Entry(left_frame)
date_box.grid(row=1, column=1)

def take_input():
	subject = subject_box.get()
	date = date_box.get()
	print(subject)
	print(date)


input_button = Button(left_frame, text="INPUT", bg="skyblue", fg="white", command=take_input).grid(row=2, column=0, sticky= 'e')


right_frame= Frame(root, width=250, height= 300)
right_frame.grid(row=0, column=1, pady=10) #creates main right frame

right_frame1 = Frame(right_frame, width=205, height= 150, bg="skyblue")
right_frame1.grid(row=0, column=1, padx=10, pady=10) #creates the right top frame used to display the database

show_database_button = Button(right_frame1, text="Show database", bg="skyblue", fg="white").grid(row=0)
#database_display = Label(right_frame1, text=data) #here data will be assigned after the retireval process is done

#def show_database():


right_frame2 = Frame(right_frame, width=205, height= 150, bg="skyblue")
right_frame2.grid(row=1, column=1, padx=10, pady=10) #creates the bottom right frame used to get reminder

get_reminder_button = Button(right_frame2, text="Get reminder", bg="skyblue", fg="white").grid(row=0)

#def get_reminder():



root.mainloop()

