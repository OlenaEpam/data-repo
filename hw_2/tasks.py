import random
import string


# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
# Commit script to git repository and provide link as home task result.

# 1. create a list of random number of dicts (from 2 to 10)
# Determine some random number for number of dictionaries
number_of_dictionaries = random.randint(2, 10)
number_for_values = random.randint(2, 100)
# Randomly choose a letter from all the ascii_letters
randomLetter = random.choice(string.ascii_letters)
print(randomLetter)

# dict's random numbers of keys should be letter

# Create empty list to put dictionaries into it
# list_of_dictionaries = []
# a = 0
# while a <= number_of_dictionaries:
#     list_of_dictionaries.append()
#     a += 1


