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
key_counts = {}

for dict_num, dictionary in enumerate(list_of_dictionaries, start=1):
    for key, value in dictionary.items():
        if key in united_dictionary and value > united_dictionary[key][0]:
            united_dictionary[key] = (value, dict_num)
        elif key not in united_dictionary:
            united_dictionary[key] = (value, dict_num)
        key_counts[key] = key_counts.get(key, 0) + 1
final_dict = {f'{key}_{value[1]}' if key_counts[key] > 1 else key: value[0] for key, value in united_dictionary.items()}

print(final_dict)
