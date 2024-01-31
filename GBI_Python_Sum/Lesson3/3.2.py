# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

numbers = [input('Введите число: ') for i in range(int(input('Введите кол-во чисел: ')))]
shift = int(input('Введите число, на к-е сдвигается последовательность введенных чисел: '))

# if shift>len(numbers):
#     shift = shift-(shift//len(numbers))*len(numbers)
# numbers_shift = list()
# for i in range(len(numbers)):
#     if shift-len(numbers)<0:
#         numbers_shift.append(numbers[shift-len(numbers)-1])
#         numbers.pop(shift-len(numbers)-1)
#     else:
#         numbers_shift.append(numbers[i-shift])
# print(*numbers_shift)

for i in range(shift):
    numbers.insert(0,numbers.pop())
print(numbers)