file = open(r"C:\Users\a\Desktop\Lesson-Alarm\Lesson plan.txt")
import datetime
import pyttsx3
import time
from time import sleep

for i in file:

    list = i.split()


    if list[0] == "Monday":
        list_of_monday = list[1:]
    elif list[0] =="Tuesday":
        list_of_tuesday = list[1:]
    elif list[0] == "Wednesday":
        list_of_wednesday = list[1:]
    elif list[0] == "Thursday":
        list_of_thursday = list[1:]
    elif list[0] == "Friday":
        list_of_friday = list[1:]
    elif list[0] == "lesson_alarm":
        lesson_alarm = list[1:]
while True:
    sleep(1)
    now = datetime.datetime.now()
    day = now.strftime("%A")
    day = day.upper()
    print(now, day)
    time = now.strftime("%H.%M")
    print(time)
    engine = pyttsx3.init()
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.zosia.premium")
    rate = engine.getProperty("rate")
    engine.runAndWait()


    if time in lesson_alarm:
        print("Rozpoczela sie lekcja")

        match day:
            case "MONDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_monday[index_of_alarm])
                tekst = "Rozpoczeła sie lekcja " + list_of_monday[index_of_alarm]
                engine.say(tekst)
            case "TUESDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_tuesday[index_of_alarm])
            case "WEDNESDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_wednesday[index_of_alarm])
            case "THURSDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_thursday[index_of_alarm])
            case "FRIDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_friday[index_of_alarm])
        sleep(60)






print(list)
file.close()


