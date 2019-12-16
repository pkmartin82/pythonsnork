from datetime import datetime, timedelta

# the .now() function returns a datetime object
current_date = datetime.now()

print("Today is {}".format(current_date))

# timedelta function example
one_day = timedelta(days=1)
yesterday = current_date - one_day

print("Yesterday was {}".format(yesterday))

thirty_six_hours = timedelta(days = 1.5)
day_and_a_half_ago = current_date - thirty_six_hours

print("Day and a half ago = {0}".format(day_and_a_half_ago))

