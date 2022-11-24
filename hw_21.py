from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

name_pattern = r'([А-Я][а-я]*)[\s|,]([А-Я][а-я]*)[\s|,]?([А-Я][а-я]*)?'
phone_pattern = r'(\+7|8)\s?(\(?)(\d{3})(\s?\)?\-?)(\s?\-?)(\d{3})(\s?\-?)(\d{2})(\s?\-?)(\d{2})\s?\(?(доб.)?\s?(\d*)'
sub_phone_pattern = r'+7(\3)\6-\8-\10 \11\12 '

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  text = ''
  for person in contacts_list:
        text += '\n'
        for name in person:
            text += f'{name} '
  print(text)
  name_result = re.findall(name_pattern, text)
  phone_result = re.findall(phone_pattern, text)
  text_result = re.sub(phone_pattern, sub_phone_pattern, text)
  print(name_result)
  print(phone_result)
  print(text_result)

#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)

