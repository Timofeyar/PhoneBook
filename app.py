import json
from func.delete import one_d, all_d
from func.edit import number_e, name_e
from func.add import numbers_a, name_a
from func.see import all_s, one_s

with open("contacts.txt", "r", encoding="utf-8") as f:
    contacts = json.load(f)
commands = ['add', 'add_number', 'edit_name', 'edit_number', 'see_one', 'see_all', 'delete_one', 'delete_all',
            'end']
print("Команды, которые мы имеем:", *commands)
while True:

    key_word = input("Введите команду: ")
    if key_word == commands[0]:
        contacts = name_a(contacts)

    if key_word == commands[6]:
        contacts = one_d(contacts)

    if key_word == commands[2]:
        contacts = name_e(contacts)

    if key_word == commands[3]:
        contacts = number_e(contacts)

    if key_word == commands[4]:
        contacts = one_s(contacts)

    if key_word == commands[5]:
        contacts = all_s(contacts)

    if key_word == commands[1]:
        contacts = numbers_a(contacts)

    if key_word == commands[7]:
        contacts = all_d

    if key_word == commands[8]:
        with open("contacts.txt", "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
        break

