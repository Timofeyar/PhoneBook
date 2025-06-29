from func.normalize import normalize_name


def one_d(contacts):

    print(*contacts.keys(), sep=", ")
    name = normalize_name(input("Введите имя контакта, который хотите удалить: "))
    if name in contacts:
        del contacts[name]
        print(f"Контакт '{name}' удалён.")
    else:
        print(f"Контакта с именем '{name}' не существует.")
    return contacts

def all_d(contacts):
    contacts.clear()
    print("Контакты удалены.")
    return contacts