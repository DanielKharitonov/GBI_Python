## Функции:
# def sum_numbers(n, m = 'Hello'):  # можно задать значение аргумента по умолчанию
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum
# print(sum_numbers(5))             # если не передаем значение аргумента, то он будет принят по умолчанию
# print(sum_numbers(5,'By'))

# def sum_str(*n):        # если кол-во аргументов неизвестно
#     res = ''
#     for i in n:
#         res += i
#     return res
# print (sum_str('q','we', 'r'))

## Модульность:
# import Lec3_modul1              # импорт модуля в программу
# print(Lec3_modul1.max1(5,9))    # обращение к функции при импорте только модуля
 
# import Lec3_modul1 as m1        # преименование модуля в используемой программе
# print(m1.max1(5,9))    

# from Lec3_modul1 import max1    # импорт определенной функции модуля
# print(max1(5,9))

# from Lec3_modul1 import *       # импорт всех функций модуля
# print(max1(5,9))

# # Рекурсия:

# def fibonachi(n):
#     if n in [1,2]:
#         return 1
#     return fibonachi(n-1) + fibonachi(n-2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fibonachi(i))
# print(list_1)
 
# # Быстрая сортировка

# def quick_sort(array):
#     if len(array)<=1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([1,5,66,8,4,2,58,4,3])) 

# # Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)