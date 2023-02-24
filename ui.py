from logger import input_data, print_data, filter_data, update_data, delete_data, is_number_line, get_number_max_line

def interface():
    print("""Выберите режим работы: 
             1 - запись данных,
             2 - вывод данных,
             3 - поиск данных по параметрам
             4 - изменение данных
             5 - удаление данных
             6 - максимальный номер строки
             7 - проверка наличия номера строки
             """)
    command_number = int(input("Введите номер команды: "))
    while command_number < 1 or command_number > 7:
        print("Введите корректный номер команды: ")
        command_number = int(input("Введите номер команды: "))

    if command_number == 1:
        input_data()
    elif command_number == 2:
        print_data()
    elif command_number == 3:
        print("Введите параметры поиска через ';': ")
        filter_string = input()
        filter_data(filter_string)
    elif command_number == 4:
        number_line = int(input("Введите номер строки для изменения: "))             
        while  not is_number_line(number_line):
            number_line = int(input("Введите корректный номер строки: "))
        update_data(number_line)
    elif command_number == 5:
        number_line = int(input("Введите номер строки для удаления: "))                       
        while not is_number_line(number_line):
            number_line = int(input("Введите корректный номер строки: "))
        delete_data(number_line)  
    elif command_number == 6:
        print(f"максимальный номер строки: {get_number_max_line()}")
    elif command_number == 7:
        number_line = int(input("Введите номер строки: "))
        if is_number_line(number_line):
            print("С таким номером есть строка: ")
        else:
            print("Нет такой строки: ")