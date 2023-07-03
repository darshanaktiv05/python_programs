# third program
import datetime
import random

print(random.randrange(0, 6))
print(random.randrange(5, 10))
print(random.randrange(0, 10, 3))

start_dt = datetime.date(2020, 1, 1)
end_dt = datetime.date(2023, 1, 1)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)
print(random_date)
