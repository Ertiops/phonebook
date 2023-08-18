import crud

avaliable_actions = ['просмотреть','добавить', 'найти', 'редактировать', 'удалить']


running = True

while running is True:

    action = None

    while action not in avaliable_actions:
        if action is not None:
            print('Такого действия нет')

        print('введите действие:\n\n',
        'просмотреть\n',
        'добавить\n',
        'найти\n',
        'редактировать\n',
        'удалить\n')

        action = str(input())

    if action == 'добавить':

        add_action = True

        while add_action is True:

            print('\n\nвведите данные:\n')

            print('Имя:')
            first_name = input()
            print('\n')

            print('Фамилия:')
            last_name = input()
            print('\n')

            print('Отчество:\n')
            patronymic = input()
            print('\n')

            print('Организация:\n')
            organisation = input()
            print('\n')

            print('Рабочий телефон:\n')
            work_number = input()
            print('\n')

            print('Личный телефон:\n')
            personal_number = input()
            print('\n')

            crud.add_data(first_name, last_name, patronymic, organisation, work_number, personal_number)
            print('Данные добавлены успешно\n\n')
            
            answer = None

            while answer not in ['да', 'нет']:
            
                if answer is not None:
                    print("Такого действия нет\n")

                print('Добавить еще запись? (да/нет)\n\n')                    
                answer = input()

            if answer == 'нет':
                add_action = False

    elif action == 'просмотреть':

        get_action = True

        while get_action is True:
            print('Введите номер страницы\n\n')

            page_number = int(input())
            data = get_paginated_data(page_number)

            if data is None:
                print("Страницы с данным номером не существует\n\n")
            else:
                print(data, '\n\n')


            answer = None

            while answer not in ['да', 'нет']:
            
                if answer is not None:
                    print("Такого действия нет\n")

                print("Хотите просмотреть еще какую-нибудь страницу? (да/нет)\n\n")                    
                answer = input()

            if answer == 'нет':
                get_action = False

            










    running = False

print('конец')




