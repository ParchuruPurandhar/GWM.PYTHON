#import datetime and playsound modules
import datetime
import time
from playsound import playsound
#using def function set the alaram_time
def set_alarm(alarm_time):
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        if current_time==alarm_time:
            print("It's alarm time")
            print("Play the alarm")
            playsound("C:\\Users\\anil\\Downloads.Alarm")
            break
        time.sleep(1)
#Assigned time formats:%H:%M:%S,%H:%M
time_formats=["%H:%M:%S","%H:%M"]
print("Assigned time formats:")
for i,time_format in enumerate(time_formats,start=1):
    print(str(i)+""+ time_format)
choice=int(input("Enter your choice:"))
#Get the alarm time based on the selected format
selected_format=time_formats[choice-1]
alarm_time=input("Enter the alarm time("+ selected_format +"):")
if selected_format=="%H:%M:%S":
    alarm_time=datetime.datetime.strptime(alarm_time,"%H:%M:%S").strftime("%H:%M:%S")
if selected_format=="%H:%M":
    alarm_time=datetime.datetime.strptime(alarm_time,"%H:%M").strftime("%H:%M:%S") 
#start the alaram
set_alaram(alarm_time)       