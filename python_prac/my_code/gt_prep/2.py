# In the code below, we've created two dates. The day in each
# date is chosen randomly. You don't need to worry about how
# this works; all you need to know is that when you start
# writing your code, you'll have access to two variables, each
# holding a date: earlier_date and later_date, and later_date
# is guaranteed to be later than earlier_date.
#
# Complete this code so that it creates a variable called
# days_between that stores the number of days between the two
# dates.
#
# Hint: You can find the number of days between two dates by
# subtracting the day number of the earlier date from the
# day number of the later date.

from datetime import date 
import random 

earlier_date = date(2017, 6, random.randint(1, 25))
later_date = date(2017, 6, random.randint(earlier_date.day +1, 28))

days_between = later_date - earlier_date
print("there are", days_between, "days between", earlier_date, "and", later_date)