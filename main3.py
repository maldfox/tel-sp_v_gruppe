# Создать контакт
def add_contact():
    book = open("phone_book.txt", "a+", encoding="utf-8")
    fio = input("Введите имя: ")
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    book.write(f"{fio},{number},{comment}\n")
    book.close()
    print(f"Новый контакт {fio},{number},{comment} добавлен")


# Показть все контакты
def all_contacts():
    with open("phone_book.txt", "r+", encoding="utf-8") as book:
        return book.readlines()


# обработка несуществующего контакта для поиска
def not_contact():
    print("Такого контакта нет, хотите его созадть?")
    add = input("Да или Нет →  ").lower()
    if add == "да":
        add_contact()


# Найти контакт
def find_contact():
    book = all_contacts()
    flag = False
    if (
        what := input(
            "Что будем искать?\nУкажите номер из списка: 1-фио, 2-номер, 3-комментарий → "
        )
    ) == "1":
        fio = input("Введите имя: ")
        for line, contact in enumerate(book):
            if fio in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    elif what == "2":
        number = input("Введите номер: ")
        for line, contact in enumerate(book):
            if number in contact.lower().split(",")[1]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    elif what == "3":
        comment = input("Введите комментарий: ")
        for line, contact in enumerate(book):
            if comment in contact.lower().split(",")[2]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    else:
        print("Нужно выбрать 1, 2 или 3")
        find_contact()


# Изменить контакт
def change_name():
    book = all_contacts()
    flag = False
    if (
        what := input(
            "Что будем менять?\nУкажите номер из списка: 1-фио, 2-номер, 3-комментарий? → "
        )
    ) == "1":
        fio = input("Кого будем менять: ").lower()
        for line, contact in enumerate(book):
            if fio in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("введите № id кого меняем?: "))
            new_name = input("Введите новое имя для контакта: ")
            book[name_id] = f'{new_name},{contact.split(",")[1]},{contact.split(",")[2]}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()

    elif what == "2":
        number = input("Введите номер: ").lower()
        for line, contact in enumerate(book):
            if number in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("введите № id кого меняем?: "))
            number = input("Введите новое имя для контакта: ")
            book[name_id] = f'{contact.split(",")[0]},{number},{contact.split(",")[2]}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()

    elif what == "3":
        comment = input("Введите комментарий: ").lower()
        for line, contact in enumerate(book):
            if comment in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("введите № id кого меняем?: "))
            comment = input("Введите новое имя для контакта: ")
            book[name_id] = f'{contact.split(",")[0]},{contact.split(",")[2]},{comment}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()
    else:
        print("Нужно выбрать 1, 2 или 3")
        change_name()
    content()

# Удалить контакт
def delete_contact():
    book = all_contacts()
    flag = False
    fio = input("Кого будем удалять?: ").lower()
    for line, contact in enumerate(book):
            if fio in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
    if flag:
        name_id = int(input("введите № id кого удаляем → "))
        print(f"{book.pop(name_id)} удален!")
        file = open("phone_book.txt", "w", encoding="utf-8")
        for contacts in book:
            file.write(str(contacts))
        file.close()
    else:
        not_contact()


# Работа справочника
def content():
    menu = {
        1: "1 → Показать все контакты",
        2: "2 → Создать новый контакт",
        3: "3 → Найти контакт",
        4: "4 → Изменить контакт",
        5: "5 → Удалить контакт",
        6: "6 → Выйти из программы",
        7: ("*" * 26),
    }
    print()
    print("*" * 7, "Содержание", "*" * 7)
    print(*menu.values(), sep="\n")
    point = int(input("\nВведите № пункта → "))   
    if point == 1:  # Показать все контакты
        contact_list = []
        for contact in all_contacts():
            contact = contact.rstrip().split(",")
            contact_list.append(" ".join(contact))
        contact_list.sort()
        print(*contact_list, sep="\n")  # выводим отсортированный по алфавиту справочник
        content()
    elif point == 2:  # Создать новый контакт
        add_contact()
        content()
    elif point == 3:  # Найти контакт
        find_contact()
        content()
    elif point == 4:  # Изменить контакт
        change_name()
        content()
    elif point == 5:  # Удалить контакт
        delete_contact()
        content()
    elif point == 6:  # Выйти из программы
        exit()


# Запуск программы
content()