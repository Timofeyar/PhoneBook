from func.normalize import normalize_name, normalize_number


def name(contacts):
    print(*contacts.keys(), sep=", ")
    name = normalize_name(input("Введите имя контакта для редактирования: "))

    if name in contacts:
        new_name = normalize_name(input("Введите новое имя (оставьте пустым, чтобы оставить прежнее): "))
        if new_name:
            contacts[new_name] = contacts.pop(name)
            name = new_name
        print(f"Контакт '{name}' успешно отредактирован.")
    else:
        print(f"Контакта с именем {name} не найдено.")  # Должна быть возможность отредактировать ВСЁ
    return contacts

# добавить проверку на имя, номер.
def number(contacts):
    print(*contacts.keys(), sep=", ")
    name = normalize_name(input("Введите имя контакта для редактирования: "))
    numbers = contacts[name]
    print("Номера контакта:", end=" ")
    print(*numbers, sep=", ")
    old_number = normalize_number(input("Введите номер который хотите изменить: "))
    index_number = numbers.index(old_number[0])
    new_number = normalize_number(input("Введите новый номер: "))
    numbers[index_number] = new_number[0]
    contacts[name] = numbers
    return contacts
