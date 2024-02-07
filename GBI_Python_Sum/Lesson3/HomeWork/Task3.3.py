# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит
# либо только английские, либо только русские буквы.

english = {
    "A,E,I,O,U,L,N,S,T,R": 1,
    "D,G": 2,
    "B,C,M,P": 3,
    "F,H,V,W,Y": 4,
    "K": 5,
    "J,X": 8,
    "Q,Z": 10,
}
russian = {
    "А,В,Е,И,Н,О,Р,С,Т": 1,
    "Д,К,Л,М,П,У": 2,
    "Б,Г,Ё,Ь,Я": 3,
    "Й,Ы": 4,
    "Ж,З,Х,Ц,Ч": 5,
    "Ш,Э,Ю": 8,
    "Ф,Щ,Ъ": 10,
}

word = input("Введите русское/английское слово: ").upper()

# sum = 0
# for key in english:
#    for i in range(0,len(word)):
#         if word[i] in key:
#             sum = sum + english[key]
# for key in russian:
#    for i in range(0,len(word)):
#         if word[i] in key:
#             sum = sum + russian[key]
# print(f'Стоимость слова в очках = {sum}')

print(
    sum(
        [i[1] for i in english.items() for j in word if j in i[0]]
        + [i[1] for i in russian.items() for j in word if j in i[0]]
    )
)