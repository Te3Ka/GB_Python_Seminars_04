'''
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n

input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''

phrase = 'a a a b c a a d c d d'
list_phrase = phrase.split(' ')
print(phrase)
new_phrase = ''
dict_phrase = {}
for i in list_phrase:
    if i in dict_phrase:
        count = dict_phrase[i]
        count += 1
        dict_phrase[i] = count
        new_phrase += str(i) + '_' + str(dict_phrase[i]) + ' '
    else:
        dict_phrase[i] = 0
        new_phrase += str(i) + ' '
print(new_phrase)