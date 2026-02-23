tasks = []
while True:
    print('---- Список дел ----')
    print('1. Показать задачи')
    print('2. Добавить задачу')
    print('3. Выход')
    choice = input('Выберите действие: ')
    if choice == 3:
        print('До свидания!')
        break

    elif choice == 2:
        if not tasks:
            print('Список дел пуст')
        else:
            print(tasks)