import crud

# list of valid actions 
avaliable_actions = ['просмотреть','добавить', 'найти', 'редактировать', 'выйти']

# stores boolean to keep app running if True
running = True
# main loop that kepps app running
while running is True:
    # stores boolean to keep main functional running while app is on
    main_action = True
    # loops through main actions while user wants to use functionality
    while main_action is True:
        # stores main action value - None to provide while loop till action is not chosen
        action = None
        # loop till  main action is not chosen
        while action not in avaliable_actions:

            if action is not None:
                print('Такого действия нет')

            print('введите действие:\n\n', 'просмотреть\n', 'добавить\n',
                  'найти\n', 'редактировать\n', 'выйти\n')

            action = str(input())

        if action == 'добавить':
            # stores subaction boolean to process while loop
            add_action = True

            while add_action is True:
                print('\n\nВведите данные:\n')
                # stores validation bbolean to process while validation loop
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
                    existance_validation = crud.validate_unique_phone(work_number, 'work_number')
                    if existance_validation is True:
                        print("\nДанный номер записан у другого контакта. Введите другой номер.")
                        validation = False                    

                validation = False
                while validation is False:                
                    print('\nЛичный телефон (11 цифр):\n')
                    personal_number = input()
                    validation = crud.validate_phone(personal_number)
                    existance_validation = crud.validate_unique_phone(personal_number, 'personal_number')
                    if existance_validation is True:
                        print("\nДанный номер записан у другого контакта. Введите другой номер.")
                        validation = False



                crud.add_data(first_name, last_name, patronymic, organisation, work_number, personal_number)
                print('\nДанные добавлены успешно.\n')
                # stores answer value to process answer validatiom                
                answer = None

                while answer not in ['да', 'нет']:
                
                    if answer is not None:
                        print("\nТакого действия нет\n")

                    print('\nДобавить еще запись? (да/нет)\n')                    
                    answer = input()

                if answer == 'нет':
                    add_action = False
        # initiate condition of get action
        elif action == 'просмотреть':
            # stores subaction boolean to process while loop
            get_action = True
            # loop to get and check valid integer for pagination
            while get_action is True:
                print('\nВведите номер страницы\n')

                page_number = input()
                # check if integer is an integer
                validation = page_number.isdigit()
                # condition to process pagination if inserted value is an integer
                if validation is True:
                    # stores pandas slice by page number
                    data = crud.get_paginated_data(int(page_number))

                    if data is None:
                        print("\nСтраницы с данным номером не существует\n")
                    else:
                        print(data, '\n\n')

                    answer = None
                    # loop to check if user wants to repeat current main action
                    while answer not in ['да', 'нет']:
                    
                        if answer is not None:
                            print("\nТакого действия нет\n")

                        print("\nХотите просмотреть еще какую-нибудь страницу? (да/нет)\n")                    
                        answer = input()

                    if answer == 'нет':
                        get_action = False


        # initiate condition of update main action               
        elif action == 'редактировать':
            # stores subaction boolean to process while loop
            update_action = True

            while update_action is True:
                print('\nВведите номер телефона, чтобы отредактировать запись\n')
                # stores imput number to process search in database
                former_number = input()

                number_validation = crud.check_number(former_number) 

                if number_validation is False:
                    print("\nЗаписи по данному номеру не существует. Хотите найти запись по другому номеру? (да/нет)\n")

                    answer = None
                    while answer not in ["да", "нет"]:

                        if answer is not None:
                            print("\nТакого действия нет\n")

                        answer = input()

                        if answer == 'нет':
                            update_action = False


                else:                          
                    print('\n\nВведите данные для изменения (нажмите Enter, чтобы пропустить редактирование любого поля):\n')


                    print('Имя:')
                    first_name = crud.validate_updated_string(input())

                    print('\nФамилия:')
                    last_name = crud.validate_updated_string(input())

                    print('\nОтчество:\n')
                    patronymic = crud.validate_updated_string(input())

                    print('\nОрганизация:\n')
                    organisation = crud.validate_updated_string(input())
                    

                    work_number = False
                    while work_number is False:
                        print('\nРабочий телефон (11 цифр):\n')
                        work_number = crud.validate_phone_update(input())

                        existance_validation = crud.validate_unique_phone(work_number, 'work_number')
                        if existance_validation is True:
                            print("\nДанный номер записан у другого контакта, либо повторяет текущий. Введите другой номер.")
                            work_number = False  
                    

                    personal_number = False
                    while personal_number is False:
                        print('\nЛичный телефон (11 цифр):\n')
                        personal_number = crud.validate_phone_update(input())

                        existance_validation = crud.validate_unique_phone(personal_number, 'personal_number')
                        if existance_validation is True:
                            print("\nДанный номер записан у другого контакта, либо повторяет текущий. Введите другой номер.")
                            personal_number = False    


                    crud.update_data(first_name, last_name, patronymic, organisation, work_number, personal_number, former_number)
                    print('\nЗапись обновлена успешно\n')


                    answer = None

                    while answer not in ['да', 'нет']:
                    
                        if answer is not None:
                            print("\nТакого действия нет\n")

                        print("\nХотите отредактировать еще запись? (да/нет)\n")                    
                        answer = input()

                    if answer == 'нет':
                        update_action = False
        # initiate condition of search main action
        elif action == 'найти':
            # stores subaction boolean to process while loop
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
        # initiate condition of exit main action
        elif action == 'выйти':
            print('\nВы закрыли справочник. До свидания!')
            exit()
               

        answer = None
        # exit program and its validation after main action is over
        while answer not in ['да', 'нет']:
        
            if answer is not None:
                print("\nТакого действия нет\n")

            print("\nХотите выполнить еще действие? (да/нет)\n")                    
            answer = input()

        if answer == 'нет':
            main_action = False



    running = False

print('\nВы закрыли справочник. До свидания!')




