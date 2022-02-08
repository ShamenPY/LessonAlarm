file = open(r"Lesson plan.txt")
import datetime
from time import sleep
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
    print(time)


    if time in lesson_alarm:
        print("Rozpoczela sie lekcja")

        match day:
            case "MONDAY":
                index_of_alarm = lesson_alarm.index(time)
                print(list_of_monday[index_of_alarm])
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




 
