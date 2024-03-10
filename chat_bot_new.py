from collections import UserDict
import funcs
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if name != '':
            super().__init__(name)
        elif not isinstance(name, str):
            raise TypeError(
                'You are no Elon. You must be better. Name your contacts like human being.')
        else:
            raise ValueError('Please give me a name of your contact')


class Phone(Field):
    def __init__(self, phone):
        if Phone.validate(phone):
            super().__init__(phone)
        else:
            raise ValueError('Not valid phone length. It should be 10 symbols')

    @staticmethod
    def validate(phone):
        return len(phone) == 10


class Birthday:
    def __init__(self, birthday) -> None:
        if self.validate(birthday):
            self.value = birthday
        else:
            raise TypeError('Invalid birthday type')

    @staticmethod
    def validate(date):
        return isinstance(date, datetime)


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_phone(self, phone):
        self.phones.append(phone)

    def add_birthday(self, birthday_class):
        birthday_formatted = birthday_class.value.strftime('%d.%m.%Y')
        self.birthday = birthday_formatted

    def find_phone(self, phone):
        return self.phones[self.phones.index(phone)]

    def edit_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(old_phone)] = new_phone

    def remove_phone(self, phone):
        return self.phones.pop(self.phones.index(phone))

    def get_birthday(self):
        return self.birthday

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.__str__() for p in self.phones)}, birthday: {self.birthday}"


class AddressBook(UserDict):
    def add_record(self, record):
        to_update = {record.name.__str__(): record}
        self.data.update(to_update)
        print(f'Contact {record.name} was added!')

    def find(self, name):
        if self.data.get(name, None) is None:
            return 'No such contact was found'
        else:
            return self.data[name]

    def delete(self, name):
        if self.data.get(name, None) is None:
            return 'No such contact was found'
        else:
            user = self.data.pop(name)
            return f'{user.name} was removed from your contacts!'


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            funcs.add_contact(args, book)

        elif command == "find":
            name = args[0]
            print(book.find(name))
        elif command == "delete":
            name = args[0]
            print(book.delete(name))
        elif command == "show_all":
            for name, record in book.data.items():
                print(record)

        elif command == "add_phone":
            funcs.add_phone(args, book)
        elif command == "add_birthday":
            funcs.add_birthday(args, book)
        elif command == "edit_phone":
            funcs.edit_phone(args, book)
        elif command == "find_phone":
            funcs.find_phone(args, book)
        elif command == "show_birthday":
            funcs.show_birthday(args, book)
        elif command == "remove_phone":
            funcs.remove_phone(args, book)
        elif command == "birthdays":
            funcs.get_birthdays_per_week(book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
