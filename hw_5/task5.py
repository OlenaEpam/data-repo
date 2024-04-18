import datetime


class NewsTool:
    def __init__(self, user_input):
        self.user_input = user_input

    def start_program(self):
        if self.user_input == '1':
            text = input("Enter text: ")
            city = input("Enter city: ")
            b = News(text, city)
            b.print_to_file()
        elif self.user_input == '2':
            text = input("Enter text: ")
            expiration_date = input("Enter expiration date (yyyy-mm-dd format): ")
            b = PrivateAdd(expiration_date, text)
            b.print_to_file()
        elif self.user_input == '3':
            text = input("Enter text: ")
            ticket_price = input("Enter ticket price without currency ($ by default) : ")
            event_date = input("Enter event date: ")
            b = Event(text, ticket_price, event_date)
            b.print_to_file()
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
            file.write(f'\nNews-------------\n Text: {self.text} \n City: {self.city} \n '
                       f'Date of publication: {datetime.date.today()}')


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


class Event(Publication):
    def __init__(self, text, ticket_price, event_date):
        Publication.__init__(self, text=text)
        self.ticket_price = ticket_price
        self.event_date = event_date

    def print_to_file(self):
        with open('newsfeed.txt', 'a') as file:
            file.write(f'\nEvent-------------\n Text: {self.text} \n Ticket price: {self.ticket_price}$ '
                       f'\n Event date: {self.event_date}')


a = NewsTool(input('Select type: 1 - News, 2 - Private add, 3 - Event: '))
a.start_program()
