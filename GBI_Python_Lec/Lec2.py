# # Ввод списка:
# list_1 = []
# list_1 = list()
# list_1 = [1,8,3,5,9]

# # Вывод в списка:
# print (list_1)  #- вывод списка в квадратных скобках
# print (*list_1) #- вывод списка без квадртных скобок

# for i in list_1:
#     print(i)

# print(len(list_1))
# print(list_1[2])

# # Функции для работы со списками:
# list_1 = [1,5]
# list_1.append(8) # - .append() добавляет указанный элемент в конце списка
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1 )

# list_1 = [1,12,5,6,-2,5]
# print(list_1)
# list_1.pop() # - .pop() удаляет последний элемент из списка
# print(list_1)
# list_1.pop(0) # - .pop(n) удаляет n-й элемент из списка
# print(list_1)
# print(list_1.pop()) # - .pop() в print - вывод удаляемого элемента
# print(list_1)

# list_1 = [1,12,5,6,-2,5]
# print(list_1)
# list_1.insert(1,333) # - .insert(i,n) - добавляет на i-ю позицию n-й элемент
# print(list_1)

# # Работа с кортежами

# t = ()          # - пустой кортеж (class tuple)
# print(type(t))

# t = (1,)        # - кортеж с значениями, в конце обязательно наличие запятой
# print(type(t))

# v = [1,2,3]
# print(type(v))  
# v = tuple(v)      # - перевод списка в кортеж (calss list in tuple)
# print(type(v))

# a=1
# b=2
# a, b = 1, 2       # - множественное присваивание

# a,b,c = v         # - распаковка кортежа (присваивание переменным элементов кортежа)
# print (a,b,c)

# # Работа со словарями
# d = {}              # - пустой словарь
# d = dict()          # - пустой словарь

# d['q'] = 'qwerty'   # - добавление ключа и элемента в словарь
# print(d)            # - вывод всего словаря

# d['w'] = 'werty'
# print(d)
# print(d['q'])       # - вывод элемента словаря по ключу

# del d['q']          # - удаление элемента из словаря по ключу
# print(d)

# dictionary = {'up': 'Вверх', 'down': 'Вниз', 'left': 'Влево'}
# for item in dictionary:
#     print('{}: {}'.format(item,dictionary[item]))

# for (k,v) in dictionary.items(): # - dictionary.items() представленеи словаря в виде набора кортежей состоящих из ключа и элемента
#         print(k,v)

