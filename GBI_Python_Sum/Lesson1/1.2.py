# В некоторой школе решили набрать три новых математических 
# класса и оборудовать кабинеты для них новыми партами. За
# каждой партой может сидеть два учащихся. Известно количество
# учащихся в кадом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрети для них.

class1 = int(input('Количество учащихся в 1 классе: '))
class2 = int(input('Количество учащихся в 2 классе: '))
class3 = int(input('Количество учащихся в 3 классе: '))

min_table_class = ((class1+1)//2)+((class2+1)//2)+((class3+1)//2) 

print (min_table_class)