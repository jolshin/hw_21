from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

name_pattern = r'([А-Я][а-я]*)[\s|,]{1}([А-Я][а-я]*)+[\s|,]{1}([А-Я][а-я]*)?'
phone_pattern = r'(\+7|8)\s?(\(?)(\d{3})(\s?\)?\-?)(\s?\-?)(\d{3})(\s?\-?)(\d{2})(\s?\-?)(\d{2})\s?\(?(доб.)?\s?(\d*)'

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  
  result_list = []

  for person in contacts_list:
        text = ''
        phone = 'phone'
        f_name = 'firstname'
        l_name = 'lastname'
        surname = 'surname'

        #make a string from rows
        for name in person:
            text += f'{name},'

        #find a certain piece of text with name
        result_names = re.search(name_pattern, text)

        #if *names are found then assign them to vars
        if result_names:
            surname = result_names.group(1)
            f_name = result_names.group(2)
            l_name = result_names.group(3)
        
        #find a certain piece of text with phone
        result_phones = re.search(phone_pattern, text)
        
        #if phone is found then assign it to a variable with a certain format
        if result_phones:
            if result_phones.group(11):
                phone = '+7('+result_phones.group(3)+')'+result_phones.group(6)+'-'+result_phones.group(8)+'-'+\
                    result_phones.group(10)+' '+result_phones.group(11)+''+result_phones.group(12)
            else:
                phone = '+7('+result_phones.group(3)+')'+result_phones.group(6)+'-'+result_phones.group(8)+'-'+\
                    result_phones.group(10)

        #check if a person with a certain firstname and surname is already in the list        
        match = [x for x in result_list if x[0] == surname and x[1] == f_name]

        #if a person is not in then append the list with data
        if match == []:
            result_list.append([surname, f_name, l_name, phone])

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result_list)