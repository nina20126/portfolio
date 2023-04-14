'''
User gives the speed of the car (km/h) and the distance (km). Program calculates amount of time.
a) in hours
b) in whole hours and minutes
'''
import math

speed = int(input("Speed (km/h):"))
distance = int(input("Distance (km):"))

time_a = distance // speed
time_b = distance / speed

minutes = time_b * 60
minutes_left = minutes - (time_a * 60)

minutes_rounded = math.floor(minutes_left)

seconds = time_b * 3600
seconds_left = seconds - (time_a * 3600) - (minutes_rounded * 60)

seconds_rounded = math.floor(seconds_left)

print(f"When the speed is {speed} km/h and distance is {distance} km, it takes...")
print(f"a) {time_a} hours")

print(f"b) {time_a} hours and {minutes_rounded} minutes and {seconds_rounded} seconds.")
