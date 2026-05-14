from datetime import datetime
now = datetime.now()
print (now)
print (now.year)
print(now.strftime("%D %b %y"))
print(now.strftime("%H:%M:%S"))
from datetime import date
birthday = date (2013, 6, 20)
today= date.today()
age_days = (today - birthday)
age_years = round(age_days.days / 365)
print (f"{age_days}")
print (f"{age_years}")

