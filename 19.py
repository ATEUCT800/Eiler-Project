from datetime import date
from datetime import timedelta

starting_date = date(1901, 1, 1)
ending_date = date(2000, 12, 31)

days_count = (ending_date - starting_date).days + 1
date_list = [starting_date + timedelta(days=x) for x in range(days_count)]

print(sum(1 for iter_date in date_list if iter_date.weekday() == 6 and iter_date.day == 1))