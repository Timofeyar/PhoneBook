

def normalize_number(numbers):
    correct_numbers = []
    numbers = numbers.replace(" ", "")
    numbers = numbers.replace("+7", "8")
    for number in numbers.split(","):
        if len(number) == 11:
            number = "8" + number[1:]
            correct_numbers.append(number)
    return correct_numbers


def normalize_name(name):
    name = name.replace(" ", "")
    return name[0].upper() + name[1:].lower()


contacts = {"Александр": ["89632536781", "89366518742"],
            "Мария": ["89026997800"],
            "Егор": ["87654563299"]}
while True:
    key_word = input("Введите команду: ")
    if key_word == 'add':  # Добавление контакта
        name = normalize_name(input("Введите имя контакта: "))
        if name in contacts:
            print("Уже есть это имя")
        else:
            phone = normalize_number(input(
                "Введите номера контакта через запятую: "))  # Написать функцию которая будет приводить номера к стандартизированному виду: (8 *** *** ****)
            contacts[name] = phone



    if key_word == 'delete':  # Удаление контакта
        print(*contacts.keys(), sep=", ")
        name = normalize_name(input("Введите имя контакта, который хотите удалить: "))
        if name in contacts:
            del contacts[name]
            print(f"Контакт '{name}' удалён.")
        else:
            print(f"Контакта с именем '{name}' не существует.")

    if key_word == 'edit_name':
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

    if key_word == "edit_number":
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

    if key_word == 'see':
        print(*contacts.keys(), sep=", ")

        name = normalize_name(input("Введите имя контакта для просмотра: "))

        if name in contacts:
            print(f"{name}: {', '.join(contacts[name])}")
        else:
            print(f"Контакта с именем {name} не найдено.")

    if key_word == 'all_see':
        for name, phones in contacts.items():
            print(f"{name} -", end=" ")
            print(*phones, sep=", ")
        # Хочу видеть весь список контактов
    if key_word == 'add_n':  # Добавить номер
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

    if key_word == 'delete_all':
        contacts.clear()
        print("Контакты удалены.")

    if key_word == 'end':
        break
print(contacts)
