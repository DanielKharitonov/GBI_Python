# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках
# записаны N целых чисел Ai. Последняя строка содержит число X

volume_numbers = int(input('Кол-во чисел: '))
while volume_numbers<=0:
    print ('Кол-во чисел указано не верно, повторите ввод:')
    volume_numbers = int(input('Кол-во чисел: '))

import random
array_numbers = [int(random.random()*10-random.random()*10) for i in range(volume_numbers)]
print(f'Массив чисел: {array_numbers}')
search_number = int(input('Введите к какому числу нужно найти ближайшее нименьшее: '))
array_numbers = [i for i in array_numbers if i < search_number]
array_numbers.sort()

print(f'Ближайшее наименьшее: {array_numbers.pop()}')