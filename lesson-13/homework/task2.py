from _datetime import datetime

birth_date = input("Input your birth date(DD-MM-YYYY):")
date_obj = datetime.strptime(birth_date, "%d-%m-%Y")
date_thisYear = datetime.strptime(f"{date_obj.day}-{date_obj.month}-{datetime.today().year}", "%d-%m-%Y")
print(date_thisYear - datetime.today())
