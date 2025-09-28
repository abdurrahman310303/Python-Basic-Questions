import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

today = datetime.date.today()
print(today)
print(today.strftime("%B %d, %Y"))

current_time = datetime.time(14, 30, 45)
print(current_time)

specific_datetime = datetime.datetime(2025, 1, 6, 15, 30, 0)
print(specific_datetime)

future_date = today + datetime.timedelta(days=30)
print(future_date)

past_date = now - datetime.timedelta(hours=5, minutes=30)
print(past_date)

birth_date = datetime.date(1990, 5, 15)
age = today - birth_date
print(f"Age in days: {age.days}")

import time
timestamp = time.time()
print(f"Timestamp: {timestamp}")
print(datetime.datetime.fromtimestamp(timestamp))
