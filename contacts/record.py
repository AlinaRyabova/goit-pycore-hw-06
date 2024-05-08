from contacts.phone import Phone
from contacts.name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(str(phone) for phone in self.phones)}"   

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone] 

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone

    def find_phone(self, phone):
        return next((p for p in self.phones if str(p) == phone), None)                    