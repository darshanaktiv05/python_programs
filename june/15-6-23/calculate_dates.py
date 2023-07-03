# second program
from datetime import date

start_date = date(2022, 12, 5)
end_date = date(2023, 1, 20)

# print(type(start_date))
num_of_days = end_date - start_date

print(num_of_days.days)
