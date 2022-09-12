from re import sub


word = input('digite uma palavra: ').lower()
word = sub(" ","",word)
word_len = len(word) - 1
adder = 0

for letter in word:
    if word[adder] != word[word_len]:
        print('Não é palíndromo.')
        exit()
    else:
        adder += 1
        word_len -= 1

print('É palíndromo!')
