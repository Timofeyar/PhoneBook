
from func.normalize import normalize_number, normalize_name


def numbers_a(contacts):
    print(*contacts.keys(), sep=", ")
    name = normalize_name(input("Введите контакт, к которому хотите добавить номер: "))
    if name in contacts.keys():
        numbers_to_edit = contacts[name]
        print(*numbers_to_edit, sep=", ")
        number = normalize_number(input("Введите номер: "))
        if number[0] not in numbers_to_edit:
            numbers_to_edit.extend(number)
            contacts[name] = numbers_to_edit
        else:
            print("Номер уже есть в контактах")
    else:
        print("Такого контакта нет")
    return contacts


def name_a(contacts):
    name = normalize_name(input("Введите имя контакта: "))
    if name in contacts:
        print("Уже есть это имя")
    else:
        phone = normalize_number(input(
            "Введите номера контакта через запятую: "))
        contacts[name] = phone
    return contacts
