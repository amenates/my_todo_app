HELP = '''
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечать все добавленные задачи.
exit - выход из программы.
'''

today = []
tomorrow = []
other = []

tasks = {}

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        # print('Сегодня')
        # print(today)
        # print('Завтра')
        # print(tomorrow)
        # print('Другие')
        # print(other)
        print(tasks)
    elif command == 'add':

        date = input('Введите дату выполнения задачи: ')
        task = input('Введите название задачи: ')

        if date == 'Сегодня':
            tasks[date] = task
            # today.append(task)
            print('Задача', task, 'добавлена')
        elif date == 'Завтра':
            tasks[date] = task
            # tomorrow.append(task)
            print('Задача', task, 'добавлена')
        else:
            tasks[date] = task
            # other.append(task)
            print('Задача', task, 'добавлена')

    elif command == 'exit':
        run = False
        print('Спасибо за использование! До свидания!')
    else:
        print('Неизвестная команда')
        print(HELP)
        # run = False
        break