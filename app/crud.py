import pandas as pd

model = {'first_name': [], 
         'last_name': [], 
         'patronymic':[],
         'organisation':[],
         'work_number': [],
         'personal_number':[]}

def create_db(model):
    """Writes python 'model' datastructure to txt file that's created or located at the same path"""
    with open('db.txt', 'w', encoding="utf-8") as db:
        db.write(str(model))
        db.close

def connect_db():
    """Reads and evals data from txt file"""
    with open('db.txt', 'r', encoding="utf-8") as db:
        data = eval(db.readline())
        db.close()
    return data

def save_db(data):
    """Writes python datastructure to txt file"""
    with open('db.txt', 'w', encoding="utf-8") as db:
        db.write(str(data))
        db.close    


def add_data(first_name, last_name, patronymic, organisation, work_number, personal_number):
    """Appends data to read datastructure from txt file"""
    data = connect_db()
    data['first_name'].append(str(first_name))
    data['last_name'].append(str(last_name))
    data['patronymic'].append(str(patronymic))
    data['organisation'].append(str(organisation))
    data['work_number'].append(str(work_number))
    data['personal_number'].append(str(personal_number))
    save_db(data)


def paginate_dataframe(dataframe, page_size, page_number):
    """Provides pagination of pandas dataframe. Returns frame if page exists or None otherwise"""

    page_size = page_size

    num_rows = len(dataframe)

    if num_rows % page_size == 0:
        num_pages = num_rows / page_size

    else:
        num_pages = num_rows // page_size + 1

    if page_number > num_pages or page_number <= 0:
        return None
    
    else:
        offset = page_size*(page_number-1)

        return dataframe[offset:offset + page_size]


def get_paginated_data(page_number):
    """gets paginated list of raws from pandas dataframe by page number"""
    data = connect_db()
    data = pd.DataFrame(data)

    query = paginate_dataframe(data, 2, page_number)

      
    return query


# data = get_paginated_data(4)

# print(data)

# add_data('Илья', 'Томин', 'Сергеевич', 'КФУ', 89534086776, 89534086776)

# create_db()




