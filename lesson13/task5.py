from datetime import datetime
import time

userTime = input("Enter time(HH:MM): ")
timeObj = datetime.strptime(userTime, "%H:%M").time()
currentTime = datetime.today().time()
while timeObj > currentTime:
    currentTime = datetime.today().time()
    print(currentTime)
    time.sleep(1)
