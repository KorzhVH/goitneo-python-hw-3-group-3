from chat_bot_new import Name, Record, Phone, Birthday
from error_manager import input_error
from datetime import datetime
from collections import defaultdict


@input_error
def add_contact(args, phone_book):
    name, *user_phones = args
    username = Name(name)
    user_record = Record(username)
    for i in user_phones:
        user_phone = Phone(i)
        user_record.add_phone(user_phone)
    phone_book.add_record(user_record)


@input_error
def add_phone(args, phone_book):
    name, phone = args
    user_record = phone_book.find(name)
    phone_to_add = Phone(phone).__str__()
    user_record.add_phone(phone_to_add)
    print(user_record)


@input_error
def edit_phone(args, phone_book):
    name, old_phone, new_phone = args
    user_record = phone_book.find(name)
    phone1 = Phone(old_phone).__str__()
    phone2 = Phone(new_phone).__str__()
    user_record.edit_phone(phone1, phone2)
    print(user_record)


@input_error
def find_phone(args, phone_book):
    name, phone = args
    user_record = phone_book.find(name)
    phone_to_find = Phone(phone).__str__()
    phone_found = user_record.find_phone(phone_to_find)
    print(f'{user_record.name}: {phone_found}')


@input_error
def remove_phone(args, phone_book):
    name, phone = args
    user_record = phone_book.find(name)
    phone_to_delete = Phone(phone).__str__()
    user_record.remove_phone(phone_to_delete)
    print(user_record)


def add_birthday(args, phone_book):
    name, birthday_input = args
    user_record = phone_book.find(name)
    datetime_birthday = datetime.strptime(birthday_input, '%d.%m.%Y')
    birthday = Birthday(datetime_birthday)
    user_record.add_birthday(birthday)
    print(user_record)


def show_birthday(args, phone_book):
    name = args[0]
    user_record = phone_book.find(name)
    get_birthday = user_record.get_birthday()
    print(f'{user_record.name}\'s birthday is {get_birthday}')


def get_birthdays_per_week(phone_book):
    weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    now = datetime.today().date()
    people_to_congratulate = defaultdict(list)
    for contact in phone_book:
        birthday = datetime.strptime(phone_book[contact].birthday, '%d.%m.%Y')
        next_birthday = datetime(
            year=now.year,
            month=birthday.month,
            day=birthday.day).date()
        if next_birthday < now:
            next_birthday.replace(year=now.year + 1)
        delta_days = (next_birthday - now).days
        if 7 >= delta_days >= 0:
            weekday = next_birthday.isoweekday()
            if weekday == 6 or weekday == 7:
                weekday = 1
            people_to_congratulate[weekday].append(contact)
    for i in range(1, 6):
        if people_to_congratulate.get(i) is not None:
            names = ", ".join(people_to_congratulate[i])
            print(f'{weekdays_list[i - 1]}: {names}')
