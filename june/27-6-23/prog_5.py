from datetime import date

s_d = int(input("enter starting year: "))
e_d = int(input("enter ending year: "))

for year in range(s_d, e_d):
    print(f"Weekday of December 31, {year} is {date(year, 12, 31).strftime('%A')}.")
