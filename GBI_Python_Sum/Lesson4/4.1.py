# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string1 = input("Введите строку: ").split()

# string2 = ''
# for i in string1:
#     if string2.count(i)==0:
#         string2 = string2+i
#     else:
#         string2 = string2+i+'_'+str(string2.count(i))
# print (string2)

# dict = {}.fromkeys(string1,0)
# for i in string1:
#     if dict[i] !=0:
#         print(f'{i}_{dict[i]}', end="")
#     else:
#         print(i,end="")
#     dict[i] +=1

# print(dict)

dict = {}.fromkeys(string1,0)
for i in string1:
    print(f'{i}_{dict[i]}' if dict[i] else i, end=" ") 
    dict[i] +=1

print(dict)