# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в
# массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# volume_numbers = int(input('Кол-во чисел: '))
# while volume_numbers<=0:
#     print ('Кол-во чисел указано не верно, повторите ввод:')
#     volume_numbers = int(input('Кол-во чисел: '))

# array_numbers = list()
# for i in (range(volume_numbers)):
#     num = int(input(f'{i+1}-е число:'))
#     while num<= 0:
#         print ('Введено не натуральное число, повторите ввод:')
#         num =int(input(f'{i+1}-е число:'))
#     array_numbers.append(str(num))

# # array_numbers = ','.join([str(input(f'{i+1}-е число:')) for i in range(int(input('Кол-во чисел: ')))])

# search_number = input('Введите искомое число: ')
# count_number = (','.join(array_numbers)).count(search_number)


# print(f'Число повторяется {count_number} раз')

list_nums = [int(input(f'Введите {i+1}-е число: ')) for i in range(int(input('Введите кол-во чисел: ')))]
print(list_nums.count(int(input('Введите искомое число: '))))