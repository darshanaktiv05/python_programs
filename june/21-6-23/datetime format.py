from datetime import datetime, date, timedelta

dates = date.today()
today = datetime.today()
print(date.today())

print(today.year)
print(today.month)
print(today.day)

form1 = today.strftime("%m/%d/%y")
form2 = today.strftime("%b-%d-%Y")
form3 = today.strftime("%d/%m/%Y")
form4 = today.strftime("%B %d,%Y")

print(form1)
print(form2)
print(form3)
print(form4)

new_time = dates + timedelta(hours=1.7)
print(new_time)

next_week = dates + timedelta(weeks=1)
print(dates)
print(next_week)

