# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
sum_numbers_number = number//100 + number%100//10 + number%10
print ('Сумма чисел трехзначного числа = ', sum_numbers_number)
