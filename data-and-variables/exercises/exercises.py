# 1. Declare and assign the variables here:

shuttle_name = "Determination"
shuttle_speed_mph = 17500
distance_mars_km = 225000000
distance_moon_km = 384400
mi_per_km = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_mars_km))
print(type(distance_moon_km))
print(type(mi_per_km))

# Code your solution to exercises 3 and 4 here:

distance_mars_mi = distance_mars_km * mi_per_km
time_mars_hours = distance_mars_mi / shuttle_speed_mph
time_mars_days = time_mars_hours / 24

print(shuttle_name + " will take " + str(round(time_mars_days,1)) + " days to reach Mars.")



# Code your solution to exercise 5 here

distance_moon_mi = distance_moon_km * mi_per_km
time_moon_hours = distance_moon_mi / shuttle_speed_mph
time_moon_days = time_moon_hours / 24
print(shuttle_name + " will take " + str(round(time_moon_days,1)) + " days to reach the Moon.")
