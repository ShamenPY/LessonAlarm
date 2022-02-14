#-*- coding: utf-8 -*-
import datetime
from time import sleep
from plyer import notification
from tkinter import *
import tkinter as tk
import pygame
from pygame import mixer
# song="C:\\Users\\a\\Desktop\\PycharmProjects\\Lesson-Alarm\\musics\\cs.mp3"
# mixer.init()
# mixer.music.load(song)
# mixer.music.play()


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "Ampeross-Qetto-2-Timer.ico",
        timeout = 10,
    )

lesson_alarm = 0

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
l3=tk.Label(root,text="wyprzedzenie: ", bg="#d4d4d4")
l3.grid(row=7,column=1)

alarm1_StringVar = StringVar()
alarm2_StringVar = StringVar()
alarm3_StringVar = StringVar()
alarm4_StringVar = StringVar()
alarm5_StringVar = StringVar()
alarm6_StringVar = StringVar()
alarm7_StringVar = StringVar()
alarm8_StringVar = StringVar()
monday1_StringVar = StringVar()
monday2_StringVar = StringVar()
monday3_StringVar = StringVar()
monday4_StringVar = StringVar()
monday5_StringVar = StringVar()
monday6_StringVar = StringVar()
monday7_StringVar = StringVar()
monday8_StringVar = StringVar()
tuesday1_StringVar = StringVar()
tuesday2_StringVar = StringVar()
tuesday3_StringVar = StringVar()
tuesday4_StringVar = StringVar()
tuesday5_StringVar = StringVar()
tuesday6_StringVar = StringVar()
tuesday7_StringVar = StringVar()
tuesday8_StringVar = StringVar()
tuesday9_StringVar = StringVar()
wednesday1_StringVar = StringVar()
wednesday2_StringVar = StringVar()
wednesday3_StringVar = StringVar()
wednesday4_StringVar = StringVar()
wednesday5_StringVar = StringVar()
wednesday6_StringVar = StringVar()
wednesday7_StringVar = StringVar()
wednesday8_StringVar = StringVar()
thursday1_StringVar = StringVar()
thursday2_StringVar = StringVar()
thursday3_StringVar = StringVar()
thursday4_StringVar = StringVar()
thursday5_StringVar = StringVar()
thursday6_StringVar = StringVar()
thursday7_StringVar = StringVar()
thursday8_StringVar = StringVar()
friday1_StringVar = StringVar()
friday2_StringVar = StringVar()
friday3_StringVar = StringVar()
friday4_StringVar = StringVar()
friday5_StringVar = StringVar()
friday6_StringVar = StringVar()
friday7_StringVar = StringVar()
friday8_StringVar = StringVar()
time_to_lesson_StringVar = StringVar()


alarm1 = Entry(root,width=5,textvariable=alarm1_StringVar).grid(row=1,column=2),
alarm2 = Entry(root, width=5,textvariable=alarm2_StringVar).grid(row=1,column=3),
alarm3 = Entry(root, width=5,textvariable=alarm3_StringVar).grid(row=1,column=4),
alarm4 = Entry(root, width=5,textvariable=alarm4_StringVar).grid(row=1,column=5),
alarm5 = Entry(root, width=5,textvariable=alarm5_StringVar).grid(row=1,column=6),
alarm6 = Entry(root, width=5,textvariable=alarm6_StringVar).grid(row=1,column=7),
alarm7 = Entry(root, width=5,textvariable=alarm7_StringVar).grid(row=1,column=8),
alarm8 = Entry(root, width=5,textvariable=alarm8_StringVar).grid(row=1,column=9),

monday1 = Entry(root, width=5,textvariable=monday1_StringVar).grid(row=2,column=2),
monday2 = Entry(root, width=5,textvariable=monday2_StringVar).grid(row=2,column=3),
monday3 = Entry(root, width=5,textvariable=monday3_StringVar).grid(row=2,column=4),
monday4 = Entry(root, width=5,textvariable=monday4_StringVar).grid(row=2,column=5),
monday5 = Entry(root, width=5,textvariable=monday5_StringVar).grid(row=2,column=6),
monday6 = Entry(root, width=5,textvariable=monday6_StringVar).grid(row=2,column=7),
monday7 = Entry(root, width=5,textvariable=monday7_StringVar).grid(row=2,column=8),
monday8 = Entry(root, width=5,textvariable=monday8_StringVar).grid(row=2,column=9),

tuesday1 = Entry(root, width=5,textvariable=tuesday1_StringVar).grid(row=3,column=2),
tuesday2 = Entry(root, width=5,textvariable=tuesday2_StringVar).grid(row=3,column=3),
tuesday3 = Entry(root, width=5,textvariable=tuesday3_StringVar).grid(row=3,column=4),
tuesday4 = Entry(root, width=5,textvariable=tuesday4_StringVar).grid(row=3,column=5),
tuesday5 = Entry(root, width=5,textvariable=tuesday5_StringVar).grid(row=3,column=6),
tuesday6 = Entry(root, width=5,textvariable=tuesday6_StringVar).grid(row=3,column=7),
tuesday7 = Entry(root, width=5,textvariable=tuesday7_StringVar).grid(row=3,column=8),
tuesday8 = Entry(root, width=5,textvariable=tuesday8_StringVar).grid(row=3,column=9),
wednesday1 = Entry(root, width=5,textvariable=wednesday1_StringVar).grid(row=4,column=2),
wednesday2 = Entry(root, width=5,textvariable=wednesday2_StringVar).grid(row=4,column=3),
wednesday3 = Entry(root, width=5,textvariable=wednesday3_StringVar).grid(row=4,column=4),
wednesday4 = Entry(root, width=5,textvariable=wednesday4_StringVar).grid(row=4,column=5),
wednesday5 = Entry(root, width=5,textvariable=wednesday5_StringVar).grid(row=4,column=6),
wednesday6 = Entry(root, width=5,textvariable=wednesday6_StringVar).grid(row=4,column=7),
wednesday7 = Entry(root, width=5,textvariable=wednesday7_StringVar).grid(row=4,column=8),
wednesday8 = Entry(root, width=5,textvariable=wednesday8_StringVar).grid(row=4,column=9),
thursday1 = Entry(root, width=5,textvariable=thursday1_StringVar).grid(row=5,column=2),
thursday2 = Entry(root, width=5,textvariable=thursday2_StringVar).grid(row=5,column=3),
thursday3 = Entry(root, width=5,textvariable=thursday3_StringVar).grid(row=5,column=4),
thursday4 = Entry(root, width=5,textvariable=thursday4_StringVar).grid(row=5,column=5),
thursday5 = Entry(root, width=5,textvariable=thursday5_StringVar).grid(row=5,column=6),
thursday6 = Entry(root, width=5,textvariable=thursday6_StringVar).grid(row=5,column=7),
thursday7 = Entry(root, width=5,textvariable=thursday7_StringVar).grid(row=5,column=8),
thursday8 = Entry(root, width=5,textvariable=thursday8_StringVar).grid(row=5,column=9),
friday1 = Entry(root, width=5,textvariable=friday1_StringVar).grid(row=6,column=2),
friday2 = Entry(root, width=5,textvariable=friday2_StringVar).grid(row=6,column=3),
friday3 = Entry(root, width=5,textvariable=friday3_StringVar).grid(row=6,column=4),
friday4 = Entry(root, width=5,textvariable=friday4_StringVar).grid(row=6,column=5),
friday5 = Entry(root, width=5,textvariable=friday5_StringVar).grid(row=6,column=6),
friday6 = Entry(root, width=5,textvariable=friday6_StringVar).grid(row=6,column=7),
friday7 = Entry(root, width=5,textvariable=friday7_StringVar).grid(row=6,column=8),
friday8 = Entry(root, width=5,textvariable=friday8_StringVar).grid(row=6,column=9),
time_to_lesson = Entry(root, width=5,textvariable=time_to_lesson_StringVar).grid(row=7,column=2)




def submit():
    global alarm1_text,alarm2_text,alarm3_text,alarm4_text,alarm5_text,alarm6_text,alarm7_text,alarm8_text, dzwonki
    global monday1_text,monday2_text,monday3_text,monday4_text,monday5_text,monday6_text,monday7_text,monday8_text
    global tuesday1_text,tuesday2_text,tuesday3_text,tuesday4_text,tuesday5_text,tuesday6_text,tuesday7_text,tuesday8_text
    global wednesday1_text, wednesday2_text, wednesday3_text, wednesday4_text, wednesday5_text, wednesday6_text, wednesday7_text, wednesday8_text
    global thursday1_text,thursday2_text,thursday3_text,thursday4_text,thursday5_text,thursday6_text,thursday7_text,thursday8_text
    global friday1_text,friday2_text,friday3_text,friday4_text,friday5_text,friday6_text,friday7_text,friday8_text, time_to_lesson_text

    alarm1_text = alarm1_StringVar.get()
    print(alarm1_text)
    alarm2_text = alarm2_StringVar.get()
    print(alarm2_text)
    alarm3_text = alarm3_StringVar.get()
    print(alarm3_text)
    alarm4_text = alarm4_StringVar.get()
    print(alarm4_text)
    alarm5_text = alarm5_StringVar.get()
    print(alarm5_text)
    alarm6_text = alarm6_StringVar.get()
    print(alarm6_text)
    alarm7_text = alarm7_StringVar.get()
    print(alarm7_text)
    alarm8_text = alarm8_StringVar.get()
    print(alarm8_text)
    monday1_text = monday1_StringVar.get()
    print(monday1_text)
    monday2_text = monday2_StringVar.get()
    print(monday2_text)
    monday3_text = monday3_StringVar.get()
    print(monday3_text)
    monday4_text = monday4_StringVar.get()
    print(monday4_text)
    monday5_text = monday5_StringVar.get()
    print(monday5_text)
    monday6_text = monday6_StringVar.get()
    print(monday6_text)
    monday7_text = monday7_StringVar.get()
    print(monday7_text)
    monday8_text = monday8_StringVar.get()
    print(monday8_text)
    tuesday1_text = tuesday1_StringVar.get()
    print(tuesday1_text)
    tuesday2_text = tuesday2_StringVar.get()
    print(tuesday2_text)
    tuesday3_text = tuesday3_StringVar.get()
    print(tuesday3_text)
    tuesday4_text = tuesday4_StringVar.get()
    print(tuesday4_text)
    tuesday5_text = tuesday5_StringVar.get()
    print(tuesday5_text)
    tuesday6_text = tuesday6_StringVar.get()
    print(tuesday6_text)
    tuesday7_text = tuesday7_StringVar.get()
    print(tuesday7_text)
    tuesday8_text = tuesday8_StringVar.get()
    print(tuesday8_text)
    wednesday1_text = wednesday1_StringVar.get()
    print(wednesday1_text)
    wednesday2_text = wednesday2_StringVar.get()
    print(wednesday2_text)
    wednesday3_text = wednesday3_StringVar.get()
    print(wednesday3_text)
    wednesday4_text = wednesday4_StringVar.get()
    print(wednesday4_text)
    wednesday5_text = wednesday5_StringVar.get()
    print(wednesday5_text)
    wednesday6_text = wednesday6_StringVar.get()
    print(wednesday6_text)
    wednesday7_text = wednesday7_StringVar.get()
    print(wednesday7_text)
    wednesday8_text = wednesday8_StringVar.get()
    print(wednesday8_text)
    thursday1_text = thursday1_StringVar.get()
    print(thursday1_text)
    thursday2_text = thursday2_StringVar.get()
    print(thursday2_text)
    thursday3_text = thursday3_StringVar.get()
    print(thursday3_text)
    thursday4_text = thursday4_StringVar.get()
    print(thursday4_text)
    thursday5_text = thursday5_StringVar.get()
    print(thursday5_text)
    thursday6_text = thursday6_StringVar.get()
    print(thursday6_text)
    thursday7_text = thursday7_StringVar.get()
    print(thursday7_text)
    thursday8_text = thursday8_StringVar.get()
    print(thursday8_text)
    friday1_text = friday1_StringVar.get()
    print(friday1_text)
    friday2_text = friday2_StringVar.get()
    print(friday2_text)
    friday3_text = friday3_StringVar.get()
    print(friday3_text)
    friday4_text = friday4_StringVar.get()
    print(friday4_text)
    friday5_text = friday5_StringVar.get()
    print(friday5_text)
    friday6_text = friday6_StringVar.get()
    print(friday6_text)
    friday7_text = friday7_StringVar.get()
    print(friday7_text)
    friday8_text = friday8_StringVar.get()
    print(friday8_text)
    time_to_lesson_text = time_to_lesson_StringVar.get()
    print(time_to_lesson_text)

submitButton = Button(root, text="Zapisz", command=submit).grid(row=8,column=1)

root.mainloop()

file = open("Lesson plan.txt", "w")
if file.writable():
    file.write("lesson_alarm" + ";" + alarm1_text + ";" + alarm2_text + ";" + alarm3_text + ";" + alarm4_text + ";" + alarm5_text + ";" + alarm6_text + ";" + alarm7_text + ";" + alarm8_text + "\n")
    file.write("Monday" + ";" + monday1_text + ";" + monday2_text + ";" + monday3_text + ";" + monday4_text + ";" + monday5_text + ";" + monday6_text + ";" + monday7_text + ";" + monday8_text + "\n")
    file.write("Tuesday" + ";" + tuesday1_text + ";" + tuesday2_text + ";" + tuesday3_text + ";" + tuesday4_text + ";" + tuesday5_text + ";" + tuesday6_text + ";" + tuesday7_text + ";" + tuesday8_text + "\n")
    file.write("Wednesday" + ";" + wednesday1_text + ";" + wednesday2_text + ";" + wednesday3_text + ";" + wednesday4_text + ";" + wednesday5_text + ";" + wednesday6_text + ";" + wednesday7_text + ";" + wednesday8_text + "\n")
    file.write("Thursday" + ";" + thursday1_text + ";" + thursday2_text + ";" + thursday3_text + ";" + thursday4_text + ";" + thursday5_text + ";" + thursday6_text + ";" + thursday7_text + ";" + thursday8_text + "\n")
    file.write("Friday" + ";" + friday1_text + ";" + friday2_text + ";" + friday3_text + ";" + friday4_text + ";" + friday5_text + ";" + friday6_text + ";" + friday7_text + ";" + friday8_text)
file.close()

file = open("Lesson plan.txt", "r")

for i in file:
    line_list = i.split(";")

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

    time = now.strftime("%H.%M")
    minutes = time[-2:]
    hours = time[:2]
    minutes = str(int(minutes) + int(time_to_lesson_text))
    time = str(hours) + "." + minutes




    x = int(time_to_lesson_text) * 60
    seconds = int(hours) * 3600 + int(minutes) * 60 + x
    hours = seconds // 3600
    seconds = seconds - (hours * 3600)

    minutes = seconds // 60

    if minutes < 10:
        minutes = "0" + str(minutes)

    time = (str(hours) + "." + str(minutes))
    print(time)


    if time in lesson_alarm:
        print("Rozpoczela sie lekcja")

        match day:
            case "MONDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_monday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ{(list_of_monday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej")
                sleep(60)
            case "TUESDAY":
                (index_of_alarm)= lesson_alarm.index(time)
                print(list_of_tuesday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_tuesday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
                sleep(60)
            case "WEDNESDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_wednesday[index_of_alarm])
                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_wednesday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
                sleep(60)
            case "THURSDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_thursday[index_of_alarm])
                sleep(60)

                notifyMe(f"ROZPOCZĘŁA SIĘ {(list_of_thursday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
            case "FRIDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_friday[index_of_alarm])
                notifyMe(f"ROZPOCZELA SIE {(list_of_friday[index_of_alarm])} ", "Dołącz na lekcję jak najszybciej!")
                sleep(60)


file.close()

# hours = int(minutes) / 60
#
# seconds = int(seconds) - int(minutes) * 60
# seconds = int(minutes)
# minutes = int(seconds) / 60