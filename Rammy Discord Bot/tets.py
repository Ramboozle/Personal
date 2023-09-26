import datetime
import time

day = datetime.datetime.today().weekday()
print(day) # returns a number between 0 and 6, where 0 is Monday and 6 is Sunday

if day == 0:
    print("It's Monday")