lines = []
line = input()

while line == '' or line[-1] != '.':
    lines.append(line)
    line = input()
lines.append(line)

text = ' '.join(lines).replace(',', ' ')
text_result ='\n'.join(lines)
alth = 'qwertyuiopasdfghjklzxcvbnm'
ALTH = 'QWERTYUIOPASDFGHJKLZXCVBNM'

words = []
word = ''
i = 0

while i < len(text):

    if text[i] in alth + ALTH:

        if len(word) == 20:
            words.append(word)
            word = ''
        else:
            word += text[i]

    elif word:
        words.append(word)
        word = ''
    i += 1

if word:
    words.append(word)

words = sorted(words, key =  len, reverse = True)
k = len(max(words, key = len))
result = ''

for i in range(len(text_result)):

    if text_result[i] in alth:
        result += chr(((ord(text_result[i]) + k) - ord('a'))% 26 + ord('a'))
    elif text_result[i] in ALTH:
        result += chr(((ord(text_result[i]) + k) - ord('A'))% 26 + ord('A'))
    else:
        result += text_result[i]

print(f'Сдвиг на {k}:\n'+result)

#ABCDEFGHIG hi, my name is Dilara, my age is 18.
