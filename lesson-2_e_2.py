__author__ = 'Ходок Александр Евгеньевич'

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Нептун', 'Сатурн', 'Плутон']
list2 = ['Меркурий', 'Венера', 'Бетельгейзе', 'Альфа-центафра', 'Солнце', 'Нептун', 'Млечный путь']

for i in list1[:]:
    for x in list2[:]:
        if x == i:
            list1.remove(x)
print(list1)