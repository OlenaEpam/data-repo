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

number_of_dictionaries = random.randint(2, 10)
list_of_dictionaries = []

for dictionary in range(0, number_of_dictionaries):
    c = {}
    number_of_keys = random.randint(2, 10)
    for keys in range(0, number_of_keys):
        c[random.choice(string.ascii_letters)] = random.randint(2, 100)
    list_of_dictionaries.append(c)

print(list_of_dictionaries)

united_dictionary = {}

for dictionary in list_of_dictionaries:
    for key, value in dictionary.items():
        if key in united_dictionary.keys():
            current_value = dictionary[key]
            saved_value = united_dictionary[key]
            if current_value > saved_value:
                united_dictionary.pop(key)
                dictionary_number = int(list_of_dictionaries.index(dictionary)) + 1
                key = f"{key}_{dictionary_number}"
                united_dictionary[key] = current_value
            else:
                united_dictionary.pop(key)
                dict_number = int(list_of_dictionaries.index(dictionary))
                key = f"{key}_{dict_number}"
                united_dictionary[key] = saved_value
        else:
            united_dictionary[key] = value

print(united_dictionary)


