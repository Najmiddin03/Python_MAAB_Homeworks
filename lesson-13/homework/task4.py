from datetime import datetime, timedelta

time = input("Enter time:(HH:MM): ")
timeObj = datetime.strptime(time, "%H:%M")
utc = input("Enter timezone(UTC+H or UTC-H): ")
utc2 = input("Enter alternative timezone(UTC+H or UTC-H): ")
time_difference = int(utc[3:]) - int(utc2[3:])
new_time = timeObj - timedelta(hours=time_difference)
print(f"Time in {utc2} is {new_time.time()}")
