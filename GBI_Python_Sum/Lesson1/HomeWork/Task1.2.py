# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов
# сделал каждый ребенок, если известно, что Петя и
# Сережа сделали одинаковое количество журавликов, а
# Катя сделала в два раза больше журавликов, чем Петя
# и Сережа вместе?

s = int(input('Введите общее кол-во сделанных журавликов: '))
if s%6==0:
    print (f"Петя и Сережа сделали по {s/6} журавликов") 
    print (f"Катя сделала {(s/6)*4} журавликов")
else:
    print ('Указано не верное количество журавликов. Кто-то подкинул кукушат =))')
    