

import time

my_time = int(input("enter the time in seconde: "))

for x in range(my_time, 0, -1):
    seconde = x %60
    minute = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x / 86400) %30
    weeks = int(x / 7200) % 54
    months = int(x / 304800) %12
    years = int(x / 36004800)
    print(f"{years:02}:{months:02}:{weeks:02}:{days:02}:{hours:02}:{minute:02}:{seconde:02}")
    time.sleep(1)


print("TIME'S UP ")

