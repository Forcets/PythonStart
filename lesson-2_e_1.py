__author__ = 'Ходок Александр Евгеньевич'

fruits = ['Яблоко', 'Апельсин', 'Мандарин', 'Дыня', 'Манго']

for num, fruit in enumerate (fruits):
    print (str(num) + '.  {:>8}'.format(fruit))