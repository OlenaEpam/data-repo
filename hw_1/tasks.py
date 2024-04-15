# Create a python script:
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console 

# Import mean method from statistic module
from statistics import mean
# Import module which has sample method in it
import random

# Task1. Create list of 100 random numbers from 0 to 1000
"""Create a variable random_list, call for a method sample from random module which requires range 
and number of required numbers. The method will return a list"""
random_list = random.sample(range(0, 1000), 100)
print(f"this is random list generated: {random_list}")

# Task2. Sort list from min to max (without using sort())
# create a new empty list in which sorted numbers will lay
sorted_list = []
# minimum_number to which 'i' (every number in a list) will be compared to and which
# will increase +1 after whole 'for' cycle is passed
minimum_number = 0
while minimum_number <= 1000:
    for i in random_list:
        if i == minimum_number:
            sorted_list.append(i)
    minimum_number += 1
print(f"This is sorted list {sorted_list}")

# Task2. Calculate average for even and odd numbers
# Create 2 list: one for even and one for odd numbers:
even_numbers = []
odd_numbers = []
# determine which number is even(the one which does not leave any residual after division on 2)
# and which are odd(with residual)
for i in sorted_list:  # for every number in a list
    if i % 2 == 0:  # if number is divided without residual
        even_numbers.append(i)  # put this number in a list of even numbers
    else:
        odd_numbers.append(i)
print(f"This is a list with even numbers: {even_numbers}")
print(f"This is a list with odd numbers: {odd_numbers}")

# using mean method let's get average from list of numbers. In case of empty list, print error from Except clause
try:
    average_of_even = mean(even_numbers)
    print(f"Average of even numbers is: {average_of_even}")
except ZeroDivisionError:
    print('error: 0 even numbers in a list')

try:
    average_of_odd = mean(odd_numbers)
    print(f"Average of odd numbers is: {average_of_odd}")
except ZeroDivisionError:
    print('error: 0 odd numbers in a list')
