# По данному целому неотрицательному n вычислите значение n!
# N! = 1*2*3*...N (Произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input('Введите целое число: '))
N = 1
i = 1
while i<=n:
    N *= i
    i += 1
print(f'n! = {N}')
