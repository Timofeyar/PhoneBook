from func.normalize import normalize_name


def all_s(contacts):
    for name, phones in contacts.items():
        print(f"{name} -", end=" ")
        print(*phones, sep=", ")



def one_s(contacts):
    print(*contacts.keys(), sep=", ")

    name = normalize_name(input("Введите имя контакта для просмотра: "))

    if name in contacts:
        print(f"{name}: {', '.join(contacts[name])}")
    else:
        print(f"Контакта с именем {name} не найдено.")
