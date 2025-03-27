from _datetime import datetime

from dateutil.relativedelta import relativedelta

birth_date = input("Input your birth date(DD-MM-YYYY):")
date_obj = datetime.strptime(birth_date, "%d-%m-%Y")
difference = relativedelta(datetime.today(), date_obj)
print(f'You are {difference.years} years, {difference.months} months and {difference.days} days old')
