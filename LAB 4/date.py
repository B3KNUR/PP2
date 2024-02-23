import datetime

#Write a Python program to subtract five days from current date.

current = datetime.datetime.now()

result = current - datetime.timedelta(days=5)

print(result)


#Write a Python program to print yesterday, today, tomorrow.

current = datetime.datetime.now()
yesterday = current - datetime.timedelta(days=1)
tomorrow = current + datetime.timedelta(days=1)

print(yesterday, current, tomorrow)


#Write a Python program to drop microseconds from datetime.

current = datetime.datetime.now()

result_without = current.replace(microsecond=0)

print(result_without)


#Write a Python program to calculate two date difference in seconds.

import datetime

def date_difference_in_seconds(date1, date2):
   
    difference = date2 - date1
    return difference.total_seconds()

print("Enter the components of the first date (year, month, day, hour, minute, second):")
year1 = int(input("Year: "))
month1 = int(input("Month: "))
day1 = int(input("Day: "))
hour1 = int(input("Hour: "))
minute1 = int(input("Minute: "))
second1 = int(input("Second: "))

print("\nEnter the components of the second date (year, month, day, hour, minute, second):")
year2 = int(input("Year: "))
month2 = int(input("Month: "))
day2 = int(input("Day: "))
hour2 = int(input("Hour: "))
minute2 = int(input("Minute: "))
second2 = int(input("Second: "))

date1 = datetime.datetime(year1, month1, day1, hour1, minute1, second1)
date2 = datetime.datetime(year2, month2, day2, hour2, minute2, second2)

difference_in_seconds = date_difference_in_seconds(date1, date2)

print(difference_in_seconds)
