
string = input()

words = []
new_words = []
word = ''
i = 0

while i < len(string):

    if string[i] != ' ':
        word += string[i]
    elif word:
        words.append(word)
        word = ''

    i += 1

if word:
    words.append(word)

words.reverse()

for word in words:
    new_word = ''
    for letter in word:
        new_word = letter + new_word
    new_words.append(new_word)

print(*words)
print(*new_words)