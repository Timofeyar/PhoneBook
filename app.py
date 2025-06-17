from func.edit import number,name

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
        contacts = name(contacts)

    if key_word == "edit_number":
        contacts = number(contacts)


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
