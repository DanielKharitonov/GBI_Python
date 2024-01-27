# Дано натуральное число А>1. Определите, каким по счету
# числом Фибоначчи оно является, то есть выведите такое
# число n, что F(n)=А. Если А не является числом Фибоначчи,
# выведите число -1.

a = int(input('Введите натуральное число больше 1: '))

count = 3
fibo1 = 1
fibo2 = 1
flag = True
while flag:
    Fibo = fibo1+fibo2
    fibo1, fibo2 = fibo2, Fibo
    count += 1
    if Fibo==a:
        flag = False
    elif Fibo>a:
        flag = False
        count = -1
print(count)