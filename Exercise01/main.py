'''
Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов идущих подряд.
Слова разделены одним или большим числом пробелов.
Определите, сколько различных(!) слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
So if sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
'''
phrase = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure."
          "So if sells sea shells on the sea shore I'm sure that the shells are sea shore shells")
print(phrase)
phrase = phrase.replace('.', ' ')
list_phrase = phrase.lower().split(' ')
set_phrase = set(list_phrase)
print(len(set_phrase))
