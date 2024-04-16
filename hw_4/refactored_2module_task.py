import random
import string


# Refactor homeworks from module 2 and 3 using functional approach with decomposition.
def generate_list_of_dictionaries():
    number_of_dictionaries = random.randint(2, 10)
    list_of_dictionaries = []

    for dictionary in range(0, number_of_dictionaries):
        c = {}
        number_of_keys = random.randint(2, 10)
        for keys in range(0, number_of_keys):
            c[random.choice(string.ascii_letters)] = random.randint(2, 100)
        list_of_dictionaries.append(c)
    return list_of_dictionaries


# calling generate list of dictionaries function
generated_list = generate_list_of_dictionaries()


def unite_dictionaries(list_with_dicts):
    united_dictionary = {}
    for dictionary in list_with_dicts:
        for key, value in dictionary.items():
            if key in united_dictionary.keys():
                current_value = dictionary[key]
                saved_value = united_dictionary[key]
                if current_value > saved_value:
                    united_dictionary.pop(key)
                    dictionary_number = int(list_with_dicts.index(dictionary)) + 1
                    key = f"{key}_{dictionary_number}"
                    united_dictionary[key] = current_value
                else:
                    united_dictionary.pop(key)
                    dict_number = int(list_with_dicts.index(dictionary))
                    key = f"{key}_{dict_number}"
                    united_dictionary[key] = saved_value
            else:
                united_dictionary[key] = value

    return united_dictionary


# call unite_dictionaries function
final_dictionary = unite_dictionaries(generated_list)


print(generated_list)
print(final_dictionary)
