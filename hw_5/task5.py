import datetime
import os
import sys
from hw_4.copy_module_4_file import lower_text, text_split_by_sentence, capitalize_sentences
from task_for_module_7 import write_count_words_to_csv, write_letters_to_csv
import sqlite3


class SaveDataToDB:
    def __init__(self, connection, cursor, text):
        self.connection = connection
        self.cursor = cursor
        self.text = text

    def publish_news_to_db(self, city):
        self.connection.execute("INSERT INTO news (City, Text_field, Date_of_publication) "
                                "VALUES (?, ?, ?)", (city, self.text, datetime.date.today().strftime('%Y-%m-%d')))
        self.connection.commit()
        self.cursor.execute('select * from news')
        result = self.cursor.fetchall()
        print(result)
        self.cursor.close()
        self.connection.close()

    def publish_add_to_db(self, expiration_date):
        current_date = datetime.datetime.now()
        future_date_reformat = datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
        days_d = future_date_reformat - current_date
        remaining_days = days_d.days
        self.connection.execute("INSERT INTO private_add (Text_field, Expiration_date, Remaining_days)"
                                "VALUES (?, ?, ?)", (self.text, expiration_date, remaining_days))
        self.connection.commit()
        self.cursor.execute('select * from private_add')
        result = self.cursor.fetchall()
        print(result)
        self.cursor.close()
        self.connection.close()

    def publish_event_to_db(self, ticket_price, event_date):
        self.connection.execute("INSERT INTO events (Text_field, Ticket_price, Event_date)"
                                "VALUES (?, ?, ?)", (self.text, ticket_price, event_date))
        self.connection.commit()
        self.cursor.execute('select * from events')
        result = self.cursor.fetchall()
        print(result)
        self.cursor.close()
        self.connection.close()


class NewsTool:
    def __init__(self, user_input):
        self.user_input = user_input

    def start_program(self):
        if self.user_input == '1':
            text = input("Enter text: ")
            city = input("Enter city: ")
            b = News(text, city)
            b.print_to_file()
            connection = sqlite3.connect('publications.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS news (City text, Text_field text, Date_of_publication date)')
            connection.commit()
            object_for_db = SaveDataToDB(connection, cursor, text)
            object_for_db.publish_news_to_db(city)
        elif self.user_input == '2':
            text = input("Enter text: ")
            expiration_date = input("Enter expiration date (yyyy-mm-dd format): ")
            b = PrivateAdd(expiration_date, text)
            b.print_to_file()
            connection = sqlite3.connect('publications.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS private_add (Text_field text, '
                           'Expiration_date date, Remaining_days digit)')
            connection.commit()
            object_for_db = SaveDataToDB(connection, cursor, text)
            object_for_db.publish_add_to_db(expiration_date)
        elif self.user_input == '3':
            text = input("Enter text: ")
            ticket_price = input("Enter ticket price without currency ($ by default) : ")
            event_date = input("Enter event date: ")
            b = Event(text, ticket_price, event_date)
            b.print_to_file()
            connection = sqlite3.connect('publications.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS events (Text_field text, '
                           'Ticket_price digit, Event_date date)')
            connection.commit()
            object_for_db = SaveDataToDB(connection, cursor, text)
            object_for_db.publish_event_to_db(ticket_price, event_date)
        else:
            print('Not value value. Relaunch the program')


class Publication:
    def __init__(self, text):
        self.text = text


class News(Publication):
    def __init__(self, city, text):
        super().__init__(text)
        self.city = city

    def print_to_file(self):
        with open('newsfeed.txt', 'a') as file:
            file.write(f'\nNews-------------\n City: {self.text} \n Text: {self.city} \n '
                       f'Date of publication: {datetime.date.today()}')
        write_count_words_to_csv()
        write_letters_to_csv()


class PrivateAdd(Publication):
    def __init__(self, expiration_date, text):
        Publication.__init__(self, text=text)
        self.expiration_date = expiration_date

    def remaining_days_active(self):
        current_date = datetime.datetime.now()
        future_date_reformat = datetime.datetime.strptime(self.expiration_date, '%Y-%m-%d')
        days_d = future_date_reformat - current_date
        day_difference = days_d.days
        return day_difference

    def print_to_file(self):
        with open('newsfeed.txt', 'a') as file:
            file.write(f'\nPrivate Add-------------\n Text: {self.text} \n Expiration date: {self.expiration_date} \n '
                       f'{self.remaining_days_active()} days left')
        write_count_words_to_csv()
        write_letters_to_csv()


class Event(Publication):
    def __init__(self, text, ticket_price, event_date):
        Publication.__init__(self, text=text)
        self.ticket_price = ticket_price
        self.event_date = event_date

    def print_to_file(self):
        with open('newsfeed.txt', 'a') as file:
            file.write(f'\nEvent-------------\n Text: {self.text} \n Ticket price: {self.ticket_price}$ '
                       f'\n Event date: {self.event_date}')
        write_count_words_to_csv()
        write_letters_to_csv()


a = NewsTool(input('Select type: 1 - News, 2 - Private add, 3 - Event: '))
a.start_program()


class InputFromFile:
    def __init__(self, file_input):
        self.file_input = file_input

    def normalize_text(self, some_text):
        lowered_text = lower_text(some_text)
        split_text = text_split_by_sentence(lowered_text)
        capitalized = capitalize_sentences(split_text)
        return capitalized

    def start_program_2(self):
        with open(self.file_input, 'r') as file:
            lines = file.readlines()
        for line in lines:
            if line == '1\n':
                index_of_news = lines.index(line)
                text = self.normalize_text(lines[index_of_news+1].strip())
                city = self.normalize_text(lines[index_of_news+2].strip())
                b = News(text, city)
                b.print_to_file()
                connection = sqlite3.connect('publications.db')
                cursor = connection.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS news (City text, Text_field text, Date_of_publication date)')
                connection.commit()
                object_for_db = SaveDataToDB(connection, cursor, text)
                object_for_db.publish_news_to_db(city)
            elif line == '2\n':
                index_of_add = lines.index(line)
                text = self.normalize_text(lines[index_of_add+1].strip())
                expiration_date = lines[index_of_add+2].strip()
                b = PrivateAdd(expiration_date, text)
                b.print_to_file()
                connection = sqlite3.connect('publications.db')
                cursor = connection.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS private_add (Text_field text, '
                               'Expiration_date date, Remaining_days digit)')
                connection.commit()
                object_for_db = SaveDataToDB(connection, cursor, text)
                object_for_db.publish_add_to_db(expiration_date)
            elif line == '3\n':
                index_of_event = lines.index(line)
                text = self.normalize_text(lines[index_of_event+1].strip())
                ticket_price = lines[index_of_event+2].strip()
                event_date = lines[index_of_event+3].strip()
                b = Event(text, ticket_price, event_date)
                b.print_to_file()
                connection = sqlite3.connect('publications.db')
                cursor = connection.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS events (Text_field text, '
                               'Ticket_price digit, Event_date date)')
                connection.commit()
                object_for_db = SaveDataToDB(connection, cursor, text)
                object_for_db.publish_event_to_db(ticket_price, event_date)


if len(sys.argv) > 1:
    file_itself = sys.argv[1]
else:
    file_itself = '/Users/Olena_Pavlyushchik/Library/CloudStorage/OneDrive-EPAM/for_data_python'
    files = os.listdir(file_itself)
    for file_name in files:
        if file_name.endswith('.txt'):
            file_itself = os.path.join(file_itself, file_name)

# Uncomment if you want to run program2 - input from file
# c = InputFromFile(file_itself)
# c.start_program_2()
# os.remove(file_itself)

# parameter can be used - /Users/Olena_Pavlyushchik/data-repo/hw_5/file.txt


def test_for_duplicates_news():
    with sqlite3.connect('publications.db') as connector:
        cursor = connector.cursor()
        cursor.execute("SELECT * FROM news GROUP BY City, Text_field, Date_of_publication HAVING COUNT(*) > 1;")
        print('Duplicates for news:')
        for row in cursor.fetchall():
            print(row)
        cursor.close()


def test_for_duplicates_adds():
    with sqlite3.connect('publications.db') as connector:
        cursor = connector.cursor()
        cursor.execute("SELECT * FROM private_add GROUP BY Text_field, Expiration_date, "
                       "Remaining_days HAVING COUNT(*) > 1;")
        print('Duplicates for adds:')
        for row in cursor.fetchall():
            print(row)
        cursor.close()


def test_for_duplicates_events():
    with sqlite3.connect('publications.db') as connector:
        cursor = connector.cursor()
        cursor.execute("SELECT * FROM events GROUP BY Text_field, Ticket_price, Event_date HAVING COUNT(*) > 1;")
        print('Duplicates for events:')
        for row in cursor.fetchall():
            print(row)
        cursor.close()


test_for_duplicates_news()
test_for_duplicates_adds()
test_for_duplicates_events()
