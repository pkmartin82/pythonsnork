from datetime import datetime, timedelta

# get the current datetime
current_time = datetime.now()
print("Right now is {}".format(current_time))

fuelcells_added_per_min = 0.25
fuelcells_used_per_battle = 5
points_per_battle = 10
fuelcells_max = 50

event_end_time = datetime(2020, 2, 3, 5, 0, 0, 0)


time_remaining = event_end_time - current_time
minutes_remaining = int(time_remaining.total_seconds() / 60)

print("Event time remaining {}".format(time_remaining))
print("Minutes remaining {}".format(minutes_remaining))

fuelcells_remaining = minutes_remaining * fuelcells_added_per_min
print("Remaining fuel cells to be added {}".format(fuelcells_remaining))

possible_battles_remaining = fuelcells_remaining / 5
print("# of Remaining possible battles {}".format(possible_battles_remaining))

possible_points_remaining = possible_battles_remaining * points_per_battle
print("Possible points remaining {}".format(possible_points_remaining))

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

