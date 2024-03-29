import pandas as pd

model = {'last_name': [],
         'first_name': [],          
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
        result = dataframe[offset:offset + page_size]
        return result


def get_paginated_data(page_number):
    """gets paginated list of raws from pandas dataframe by page number"""
    data = connect_db()
    data = pd.DataFrame(data)

    query = paginate_dataframe(data, 2, page_number)

      
    return query

def check_number(personal_number):
    """Returns boolean value whether or not value exists in db column 'personal_number'"""
    data = connect_db()
    data = pd.DataFrame(data)
    result = personal_number in set(data['personal_number'])

    return result


def update_data(first_name, last_name, patronymic, organisation, work_number, personal_number, former_number):
    """Updates database by 'personal_number' field if string of an istance is not empty"""
    data = connect_db()
    data = pd.DataFrame(data)

    filt = (data['personal_number'] == former_number)

    if first_name != "":   
        data.loc[filt, 'first_name'] = first_name
    if last_name != "":        
        data.loc[filt, 'last_name'] = last_name
    if patronymic != "":
        data.loc[filt, 'patronymic'] = patronymic
    if organisation != "":
        data.loc[filt, 'organisation'] = organisation
    if work_number != "":
        data.loc[filt, 'work_number'] = work_number
    if personal_number != "":
        data.loc[filt, 'personal_number'] = personal_number

    data = data.to_dict(orient='list')
    save_db(data)

    return data

def search_data(first_name, last_name):
    """Searches a row from database by 'first_name' and 'last_name' columns"""
    data = connect_db()
    data = pd.DataFrame(data)

    data = data.query(f"first_name == '{first_name}' and last_name == '{last_name}'")

    if len(data) == 0:
        return None    
    else:
        return data


def validate_phone(phone_number):
    """Checks if input is a digit and returns boolean value"""
    if len(phone_number) == 11 and phone_number.isdigit() is True:
        return True   
    else:
        return False

def validate_string(string):
    """Checks if the string is empty or contains spaces"""
    if string == "" or " " in string:
        return False
    else:
        return True

def validate_updated_string(string):
    """checks if input is not empty and contains spaces to update in db (avoids updating with spaces)"""
    if string != "" and " " not in string:
        return string
    else:
        return ""
     
def validate_phone_update(phone_number):
    """Checks if input is a digit or empty string"""
    if len(phone_number) == 11 and phone_number.isdigit() is True or phone_number == "":
        return phone_number   
    else:
        return False
    
def validate_unique_phone(phone_number, column):
    """Returns boolean whether personal_number in database"""
    data = connect_db()
    data = pd.DataFrame(data)

    result = phone_number in data[column].unique()

    return result
