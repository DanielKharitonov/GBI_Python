# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

volume_list_numbers1 = int(input('Введите кол-во элементов 1-го множества: '))
volume_list_numbers2 = int(input('Введите кол-во элементов 2-го множества: '))

import random

list_numbers1 = [int(random.random()*100) for i in range(volume_list_numbers1)]
list_numbers2 = [int(random.random()*100) for i in range(volume_list_numbers1)]

print(*sorted((set(list_numbers1).intersection(set(list_numbers2)))))