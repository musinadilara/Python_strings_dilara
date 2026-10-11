string = input('Введите текст: ').lower()
words = []
word = ''
i = 0
alth = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'

while i < len(string):

    if string[i] in alth:
        word += string[i]
    elif word:
        words.append(word)
        word = ''
    i += 1

if word:
    words.append(word)

words_frequency = {word: words.count(word) for word in words}
result = sorted(words_frequency, key = words_frequency.get, reverse = True)
res = ', '.join(result[:5])

print('Топ-5 самых частых слов:', res +'.')

#Hello, world! world World WORLD hello hi Hi HI ou ou top ToP tOp blah balh