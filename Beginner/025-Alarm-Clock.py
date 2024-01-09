# Below is a basic, beginner-level code for an alarm clock.
import time
import playsound
from playsound import playsound
current_time = time.strftime("%H %M")
alarm_time = input("Enter the alarm time. Ex [23 00] for 11:00 PM \n")
print(current_time, alarm_time)
if current_time == alarm_time:
  playsound('Sound.mp3')

# The following code is intermediate-level code for an alarm clock.

from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_seconds == current_seconds):
                    print("Wake Up!")
                    playsound('Sound.mp3')
                    break



