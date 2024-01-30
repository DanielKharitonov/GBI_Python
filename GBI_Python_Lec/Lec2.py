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


# # Работа с множествами

# colors = set()                      # - создание пустого множества
# colors = {'red', 'green', 'blue'}   # - создание множества
# print(colors)
# colors.add('red')                   # - доавление в множество значения, если значение уже есть в множестве то оно не будет дублироваться
# print(colors)
# colors.add('gray')                  # - значение добавляется в множестно неупорядоченно
# print(colors)
# colors.remove('red')                # - удаление значения из множества, но если занчения нет в множестве то будет ошибка
# print(colors)
# colors.discard('red')               # - удаление значения из множества при его наличии, если его нет то пропускает без вывода ошибки
# print(colors)
# colors.clear()                      # - удаление всех значений из множества
# print(colors)

# # Операции с множествами

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()            # - копирование множества а в множество с
# u = a.union(b)          # - объединение множества a с множеством b
# i = a.intersection(b)   # - пересечение множества a c множеством b
# d1 = a.difference(b)    # - разность множества а и b (из а вычитаем b)
# d2 = b.difference(a)    # - разность множества b и а (из b вычитаем а)

# f = frozenset(a)        # - замороженное множество а (неизменяемое)

# # List Comprehension

# list1 = [i for i in range(1,11)]
# print (list1)
# list2 = [i for i in range(1,11) if i%2==0]
# print(list2)
# list3 = [(i,i) for i in range(1,11) if i%2==0]
# print(list3)
# list4 = [i^2 for i in range(1,11) if i%2==0]
# print(list4)

