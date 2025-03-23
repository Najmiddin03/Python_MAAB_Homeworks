from datetime import datetime, timedelta

date = input("Enter date and time(DD-MM-YYYY HH:MM): ")
date_obj = datetime.strptime(date, "%d-%m-%Y %H:%M")
duration = input("Enter duration of the meeting:(HH:MM): ")
duration_obj = datetime.strptime(duration, "%H:%M")
print(duration_obj.time())
new_datetime = date_obj + timedelta(hours=duration_obj.hour, minutes=duration_obj.minute)
print(new_datetime)
