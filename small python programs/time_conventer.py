'''
Convert seconds to hours, minutes, second
'''

import math

print("How many seconds?")

seconds_to_convert = int(input("Seconds to convert:"))

# 1 min = 60 sec
# 1 hr = 3600 sec

hours = seconds_to_convert / 3600
hours_total = math.floor(hours)

minutes = seconds_to_convert / 60
minutes_total = math.floor(minutes - (hours_total * 60))

seconds_left = seconds_to_convert - ((hours_total * 3600) + (minutes_total * 60))

print(f"{seconds_to_convert} seconds is {hours_total} hour, {minutes_total} minutes and {seconds_left} seconds.")