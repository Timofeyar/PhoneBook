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