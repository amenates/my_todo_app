import random

HELP = '''
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечать все добавленные задачи.
exit - выход из программы.
random - добавить случайную задачу на дату Сегодня.
'''

RANDOM_TASKS = ['Записаться куда-нибудь', 'Написать Гвидо письмо', 'Покормить кошку', 'Помыть машину']
run = True
tasks = {}

def add_todo(date, task):
    if date in tasks:
        # ключ date есть в словаре
        # добавляем в список задачу 
        tasks[date].append(task)
    else:
        # ключа date нет в словаре
        # создаем запись с ключом date, и помещаем в нее список задач
        tasks[date] = [task]
    print('Задача', task, 'добавлена на дату', date)

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Такой даты нет')
    elif command == 'add':
        date = input('Введите дату выполнения задачи: ')
        task = input('Введите название задачи: ')
        add_todo(date, task)
    elif command == 'exit':
        run = False
        print('Спасибо за использование! До свидания!')
    elif command == 'random':
        task = random.choice(RANDOM_TASKS)
        add_todo('Сегодня', task)
    else:
        print('Неизвестная команда')
        print(HELP)
        # run = False
        break