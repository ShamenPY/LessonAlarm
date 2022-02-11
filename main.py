file = open(r"Lesson plan.txt")
import datetime
from time import sleep
from plyer import notification
from tkinter import *
import tkinter as tk
#import tkinter as tk
from tkinter import messagebox
#Tkinker


root = tk.Tk()
root.title("CONFIG - Lesson Alarm")
root.geometry("500x300")

root.configure(background='#d4d4d4')
root.geometry("400x300")
l3=tk.Label(root,text="dzwonki", bg="#d4d4d4")
l3.grid(row=1,column=1)
l1=tk.Label(root,text="Monday",bg="#d4d4d4")
l1.grid(row=2,column=1)
l2=tk.Label(root,text="Tuesday",bg="#d4d4d4")
l2.grid(row=3,column=1)
l3=tk.Label(root,text="Wednesday", bg="#d4d4d4")
l3.grid(row=4,column=1)
l3=tk.Label(root,text="Thursday", bg="#d4d4d4")
l3.grid(row=5,column=1)
l3=tk.Label(root,text="Friday", bg="#d4d4d4")
l3.grid(row=6,column=1)
l3=tk.Label(root,text="Wyprzedzenie: ", bg="#d4d4d4")
l3.grid(row=7,column=1)

alarm1,alarm2,alarm3,alarm4,alarm5,alarm6,alarm7,alarm8 = Entry(root, width=5,).grid(row=1,column=2), Entry(root, width=5).grid(row=1,column=3), Entry(root, width=5).grid(row=1,column=4), Entry(root, width=5).grid(row=1,column=5), Entry(root, width=5).grid(row=1,column=6), Entry(root, width=5).grid(row=1,column=7), Entry(root, width=5).grid(row=1,column=8), Entry(root, width=5).grid(row=1,column=9),
monday1,monday2,monday3,monday4,monday5,monday6,monday7,monday8 = Entry(root, width=5).grid(row=2,column=2), Entry(root, width=5).grid(row=2,column=3), Entry(root, width=5).grid(row=2,column=4), Entry(root, width=5).grid(row=2,column=5), Entry(root, width=5).grid(row=2,column=6), Entry(root, width=5).grid(row=2,column=7), Entry(root, width=5).grid(row=2,column=8), Entry(root, width=5).grid(row=2,column=9),
tuesday1,tuesday2,tuesday3,tuesday4,tuesday5,tuesday6,tuesday7,tuesday8 = Entry(root, width=5).grid(row=3,column=2), Entry(root, width=5).grid(row=3,column=3), Entry(root, width=5).grid(row=3,column=4), Entry(root, width=5).grid(row=3,column=5), Entry(root, width=5).grid(row=3,column=6), Entry(root, width=5).grid(row=3,column=7), Entry(root, width=5).grid(row=3,column=8), Entry(root, width=5).grid(row=3,column=9),
wednesday1,wednesday2,wednesday3,wednesday4,wednesday5,wednesday6,wednesday7,wednesday8 = Entry(root, width=5).grid(row=4,column=2), Entry(root, width=5).grid(row=4,column=3), Entry(root, width=5).grid(row=4,column=4), Entry(root, width=5).grid(row=4,column=5), Entry(root, width=5).grid(row=4,column=6), Entry(root, width=5).grid(row=4,column=7), Entry(root, width=5).grid(row=4,column=8), Entry(root, width=5).grid(row=4,column=9),
thursday1,thursday2,thursday3,thursday4,thursday5,thursday6,thursday7,thursday8 = Entry(root, width=5).grid(row=5,column=2), Entry(root, width=5).grid(row=5,column=3), Entry(root, width=5).grid(row=5,column=4), Entry(root, width=5).grid(row=5,column=5), Entry(root, width=5).grid(row=5,column=6), Entry(root, width=5).grid(row=5,column=7), Entry(root, width=5).grid(row=5,column=8), Entry(root, width=5).grid(row=5,column=9),
friday1,friday2,friday3,friday4,friday5,friday6,friday7,friday8 = Entry(root, width=5).grid(row=6,column=2), Entry(root, width=5).grid(row=6,column=3), Entry(root, width=5).grid(row=6,column=4), Entry(root, width=5).grid(row=6,column=5), Entry(root, width=5).grid(row=6,column=6), Entry(root, width=5).grid(row=6,column=7), Entry(root, width=5).grid(row=6,column=8), Entry(root, width=5).grid(row=6,column=9),
wyprzedzenie = Entry(root, width=5).grid(row=7,column=2)

def submit():
    global alarm1,alarm2,alarm3
    alarm1 = alarm1.get()
    print(alarm1)

submitButton = Button(root, text="Zapisz", command=submit).grid(row=8,column=1)

root.mainloop()
print(alarm1)

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "Ampeross-Qetto-2-Timer.ico",
        timeout = 10,
    )

for i in file:


    line_list = i.split()

    if line_list[0] == "Monday":
        list_of_monday = line_list[1:]
    elif line_list[0] == "Tuesday":
        list_of_tuesday = line_list[1:]
    elif line_list[0] == "Wednesday":
        list_of_wednesday = line_list[1:]
    elif line_list[0] == "Thursday":
        list_of_thursday = line_list[1:]
    elif line_list[0] == "Friday":
        list_of_friday = line_list[1:]
    elif line_list[0] == "lesson_alarm":
        lesson_alarm = line_list[1:]

while True:
    sleep(1)
    now = datetime.datetime.now()
    day = now.strftime("%A")
    day = day.upper()
    print(now, day)

    time = now.strftime("%H.%M")
    minutes = time[-2:]
    hours = time[:2]
    minutes = str(int(minutes)+1)
    time = hours + "." + minutes
    print(time)


    if time in lesson_alarm:
        print("Rozpoczela sie lekcja")

        match day:
            case "MONDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_monday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ{(list_of_monday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej")
            case "TUESDAY":
                (index_of_alarm)= lesson_alarm.index(time)
                print(list_of_tuesday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_tuesday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
            case "WEDNESDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_wednesday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_wednesday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
            case "THURSDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_thursday[index_of_alarm])

                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_thursday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
            case "FRIDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_friday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_friday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")

        sleep(60)

print(list)
file.close()


 
