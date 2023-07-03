# Get total working days of the June (Excluding saturday & sunday) using datetime.

from datetime import date, timedelta
import calendar

current_month = date.today().month
current_year = date.today().year
total_days = calendar.mdays[current_month]

s_d = date(current_year, current_month, 1)
e_d = date(current_year, current_month, total_days)
tot_days = e_d - s_d
days = 0

for i in range(tot_days.days+1):
	day = s_d + timedelta(days=i)
	if day.weekday() < 5:
		days = days + 1
print("total working days of the june is: ", days)
