# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 

def sum_nums(a, b):
    res = a
    if b == 0:
        return res
    res = sum_nums(a + 1, b - 1)
    return res

print("а + b = ", sum_nums(int(input("a = ")), int(input("b = "))))
