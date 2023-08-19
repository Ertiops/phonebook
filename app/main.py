import crud

avaliable_actions = ['просмотреть','добавить', 'найти', 'редактировать']

running = True

while running is True:

    main_action = True

    while main_action is True:

        action = None

        while action not in avaliable_actions:
            if action is not None:
                print('Такого действия нет')

            print('введите действие:\n\n', 'просмотреть\n', 'добавить\n',
                  'найти\n', 'редактировать\n')

            action = str(input())

        if action == 'добавить':

            add_action = True

            while add_action is True:
                print('\n\nВведите данные:\n')

                validation = False
                while validation is False:
                    print('Имя (обязательно):')
                    first_name = input()
                    validation = crud.validate_string(first_name)

                validation = False
                while validation is False:
                    print('\nФамилия (обязательно):')
                    last_name = input()
                    validation = crud.validate_string(last_name)
                    

                print('\nОтчество (опционально):\n')
                patronymic = input()


                print('\nОрганизация (опционально):\n')
                organisation = input()
                  

                validation = False
                while validation is False:
                    print('\nРабочий телефон (11 цифр):\n')
                    work_number = input()
                    validation = crud.validate_phone(work_number)

                validation = False
                while validation is False:                
                    print('\nЛичный телефон (11 цифр):\n')
                    personal_number = input()
                    validation = crud.validate_phone(personal_number)



                crud.add_data(first_name, last_name, patronymic, organisation, work_number, personal_number)
                print('\nДанные добавлены успешно\n')
                
                answer = None

                while answer not in ['да', 'нет']:
                
                    if answer is not None:
                        print("\nТакого действия нет\n")

                    print('\nДобавить еще запись? (да/нет)\n')                    
                    answer = input()

                if answer == 'нет':
                    add_action = False

        elif action == 'просмотреть':

            get_action = True

            while get_action is True:
                print('\nВведите номер страницы\n')

                page_number = int(input())
                data = crud.get_paginated_data(page_number)

                if data is None:
                    print("\nСтраницы с данным номером не существует\n")
                else:
                    print(data, '\n\n')


                answer = None

                while answer not in ['да', 'нет']:
                
                    if answer is not None:
                        print("\nТакого действия нет\n")

                    print("\nХотите просмотреть еще какую-нибудь страницу? (да/нет)\n")                    
                    answer = input()

                if answer == 'нет':
                    get_action = False

                
        elif action == 'редактировать':

            update_action = True

            while update_action is True:
                print('\nВведите номер телефона, чтобы отредактировать запись\n')

                former_number = input()

                number_validation = crud.check_number(former_number) 

                if number_validation is False:
                    print("\nЗаписи по данному номеру не существует\n")
                else:                          
                    print('\n\nВведите данные для изменения (нажмите Enter, чтобы пропустить редактирование любого поля):\n')

                    print('Имя:')
                    first_name = input()

                    print('\nФамилия:')
                    last_name = input()

                    print('\nОтчество:\n')
                    patronymic = input()

                    print('\nОрганизация:\n')
                    organisation = input()

                    print('\nРабочий телефон:\n')
                    work_number = input()

                    print('\nЛичный телефон:\n')
                    personal_number = input()


                    crud.update_data(first_name, last_name, patronymic, organisation, work_number, personal_number, former_number)
                    print('\nДанные добавлены успешно\n')


                    answer = None

                    while answer not in ['да', 'нет']:
                    
                        if answer is not None:
                            print("\nТакого действия нет\n")

                        print("\nХотите отредактировать еще запись? (да/нет)\n")                    
                        answer = input()

                    if answer == 'нет':
                        update_action = False

        elif action == 'найти':

            search_action = True

            while search_action is True:
                print('\nВведите имя и фамилию для поиска по справочнику\n')

                print('Имя:')
                first_name = input()

                print('\nФамилия:')
                last_name = input()
                print('\n')

                query = crud.search_data(first_name, last_name) 

                if query is None:
                    print("\nВ справочнике отсутствует кто-либо с таким именем и фамилией\n")
                else:
                    print(query)

                
                answer = None

                while answer not in ['да', 'нет']:
                
                    if answer is not None:
                        print("\nТакого действия нет\n")

                    print("\nХотите произвести поиск повторно? (да/нет)\n")                    
                    answer = input()

                if answer == 'нет':
                    search_action = False



# end of main section

        answer = None

        while answer not in ['да', 'нет']:
        
            if answer is not None:
                print("\nТакого действия нет\n")

            print("\nХотите выполнить еще действие? (да/нет)\n")                    
            answer = input()

        if answer == 'нет':
            main_action = False


    running = False

print('\nСпасибо, что воспользовались нашей программой. До свидания!')




