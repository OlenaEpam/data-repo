import csv
import re
from collections import Counter
file_path_newsfeed = '/Users/Olena_Pavlyushchik/data-repo/hw_5/newsfeed.txt'


def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        return text


def count_words():
    lower_case_text = read_file(file_path_newsfeed).lower()
    no_punctuation = re.sub(r'[^\w\s]', '', lower_case_text)
    split_to_words = no_punctuation.split()
    dictionary = Counter(split_to_words)
    return dictionary


def write_count_words_to_csv():
    dictionary_to_write = count_words()
    with open('word-count.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter='-')
        for word, count in dictionary_to_write.items():
            writer.writerow([word, count])


def count_all_letters():
    lower_case_text = read_file(file_path_newsfeed).lower()
    no_punctuation = re.sub(r'[^a-zA-Z\s]', '', lower_case_text)
    characters = [c for c in no_punctuation if c != ' ' and c != '\n']
    characters_counted = Counter(characters)
    return characters_counted


def count_uppercase_letters():
    text = read_file(file_path_newsfeed)
    no_punctuation = re.sub(r'[^\D\s]', '', text)
    uppercase_characters = [c for c in no_punctuation if c.isupper()]
    uppercase_characters_counted = Counter(uppercase_characters)
    return uppercase_characters_counted


def write_letters_to_csv():
    dictionary_with_all = count_all_letters()
    dictionary_with_upper = count_uppercase_letters()
    with open('letter-count.csv', 'w') as csv_file:
        headers = ['letter', 'count_all', 'uppercase', 'percentage']
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        all_letters_in_text = 0
        for letter, count in dictionary_with_all.items():
            all_letters_in_text += count
        for letter, count in dictionary_with_all.items():
            uppercase_count = dictionary_with_upper.get(letter.upper(), 0)
            percentage = count * 100 / all_letters_in_text
            writer.writerow(
                {'letter': letter, 'count_all': count, 'uppercase': uppercase_count, 'percentage': percentage.__round__(1)})


write_letters_to_csv()
write_count_words_to_csv()
