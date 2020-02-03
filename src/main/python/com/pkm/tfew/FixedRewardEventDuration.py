from datetime import datetime, timedelta
import datetime as dt

#
# Functions
#
onDay = lambda date, day: date + dt.timedelta(days=(day-date.weekday()+7)%7)
nextDay = lambda date, day: (date + dt.timedelta(days=(day-date.weekday()+7)%7) + dt.timedelta(days=(7 if day == date.weekday() else 0))).date()

#
# Variables
#
fuelcells_added_per_min = 0.25
fuelcells_used_per_battle = 5
points_per_battle = 10
fuelcells_max = 50

# 
# Calculated Values
#
current_time = datetime.now()
event_end_time = datetime.combine(nextDay(current_time,0), dt.time(5, 0, 0, 0))
time_remaining = event_end_time - current_time
minutes_remaining = int(time_remaining.total_seconds() / 60)
fuelcells_remaining = minutes_remaining * fuelcells_added_per_min
possible_battles_remaining = fuelcells_remaining / 5
possible_points_remaining = possible_battles_remaining * points_per_battle


print("Right now is {}".format(current_time))
print ("Event will end at {}".format(event_end_time))
print("Event time remaining {}".format(time_remaining))
print("Minutes remaining {}".format(minutes_remaining))
print("Remaining fuel cells to be added: {}".format(fuelcells_remaining))
print("Possible battles remaining: {}".format(possible_battles_remaining))
print("Possible points remaining: {}".format(possible_points_remaining))





#one_day = timedelta(days=1)
#yesterday = current_time - one_day
#time_remaining_yesterday = event_end_time - yesterday
#print("Event time remaining from this time yesterday {}".format((time_remaining_yesterday)))


# timedelta function example
#one_day = timedelta(days=1)
#yesterday = current_date - one_day
#print("Yesterday was {}".format(yesterday))

#thirty_six_hours = timedelta(days = 1.5)
#day_and_a_half_ago = current_date - thirty_six_hours
#print("Day and a half ago = {0}".format(day_and_a_half_ago))

