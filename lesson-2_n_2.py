__author__ = 'Ходок Александр Евгеньевич'

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

year = int(input('Введите год:', ))
month = int(input('Введите месяц:', ))
date = int(input('Введите число:', ))
month_list = ['января', 'февраля', 'марта', 'фпреля', 'мая', 'июня', 'июля', 'августа',\
              'сентября', 'октября', 'ноября', 'декабря']
date_list = ['Первое', 'Второе', 'Третье', 'Четвертое', 'Пятое', 'Шестое', 'Седьмое',\
             'Восьмое', 'Девятое', 'Десятое', 'Одиннадцатое', 'Двенадцатое',\
             'Тринадцатое', 'Четырнадцатое', 'Пятнадцатое', 'Шестнадцатое',\
             'Семнадцатое', 'Восемнадцатое', 'Девятнадцатое', 'Двацатое', 'Двадцать первое',\
             'Двадцать второе', 'Двадцать третье', 'Двадцать четвертое', 'Двадцать пятое',\
             'Двадцать шестое', 'Двадцать седьмое', 'Двадцать восьмое', 'Двадцать девятое',\
             'Тридцатое', 'Тридцать первое']
print(date_list[date - 1], month_list[month - 1], year, 'года')
