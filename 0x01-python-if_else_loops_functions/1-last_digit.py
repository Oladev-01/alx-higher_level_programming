#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
'''
i have to get the absolute value of the number else i will be
getting wrong digit as last digit for negative numbers
'''
pos_num = abs(number)
'''
first, i have to get the last digit of the pos_num and store in a
variable last_digit so therefore in doing so, i have to account
for if the number
is a negative one or positive: for negative-
it is checked on line 10 while for positive, on line 12
'''
if number < 0:
    last_digit = (pos_num % 10) * -1
else:
    last_digit = pos_num % 10
# then i check if the pos_num is negative and last_digit is not 0
if number < 0 and last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
# we also check if the pos_num is negative and the last digit is not 0
elif number < 0 and last_digit != 0:
    print("Last digit of {} is ".format(number) +
          "{} and is less than 6 and not 0".format(last_digit))
# i check if the number itself is 0
elif number == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
# if the last_digit is == 0
elif (number > 0) and (last_digit == 0):
    print("Last digit of {} is {} and is 0".format(number, last_digit))
# then i check if the pos_num is positive and last digit is greater than 5
elif (number > 0) and (last_digit > 5):
    print("Last digit of {} is ".format(number) +
          "{} and is greater than 5".format(last_digit))

# i check if the last digit is < 6 and not == 0
elif (number > 0) and (last_digit < 6) and (last_digit != 0):
    print("Last digit of {} is ".format(number) +
          "{} and is less than 6 and not 0".format(last_digit))
