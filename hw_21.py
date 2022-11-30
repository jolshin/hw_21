from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

name_pattern = r'([А-Я][а-я]*)[\s|,]{1}([А-Я][а-я]*)+[\s|,]{1}([А-Я][а-я]*)?'
phone_pattern = r'(\+7|8)\s?(\(?)(\d{3})(\s?\)?\-?)(\s?\-?)(\d{3})(\s?\-?)(\d{2})(\s?\-?)(\d{2})\s?\(?(доб.)?\s?(\d*)'
organization_pattern = r',,(\w+),'
email_pattern = r''

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  
  result_list = [['surname', 'firstname', 'lastname', 'phone', 'organization', 'position', 'email']]


  for person in contacts_list:
        text = ''
        phone = ''
        f_name = ''
        l_name = ''
        surname = ''
        organization = ''
        position = ''
        email = ''

        #make a string from rows
        for name in person:
            text += f'{name},'

        #assign org, pos and eamil to vars by it's index in a list
        if person[3]:
            organization = person[3]
        if person[4]:
            position = person[4]
        if person[6]:
            email = person[6]

        #find a certain piece of text with name
        result_names = re.search(name_pattern, text)

        #if *names are found then assign them to vars
        if result_names:
            surname = str(result_names.group(1))
            f_name = str(result_names.group(2))
            if result_names.group(3):
                l_name = str(result_names.group(3))

        #organization = re.search(organization_pattern, re.split(name_pattern, text))
        if re.search(organization_pattern, text):
            organization = str(re.search(organization_pattern, text).group(1))
        
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
            if surname != '':
                result_list.append([surname, f_name, l_name, phone, organization, position, email])
        #if some data is in then insert existing data
        else:
            indx = result_list.index(match[0])
            if l_name != '':
                result_list[indx].pop(2)
                result_list[indx].insert(2, l_name)
            if organization != '':
                result_list[indx].pop(4)
                result_list[indx].insert(4, organization)
            if position != '':
                result_list[indx].pop(5)
                result_list[indx].insert(5, position)
            if phone != '':
                result_list[indx].pop(3)
                result_list[indx].insert(3, phone)
            if email != '':
                result_list[indx].pop(6)
                result_list[indx].insert(6, email)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result_list)