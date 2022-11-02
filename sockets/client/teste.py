from ast import literal_eval


word = str.encode(input('digita ai: '))
new_word = ''
checksum = 0

for i in word:
    checksum ^= literal_eval(hex(i))
    new_word += hex(i)
    print(hex(i), '\n')



print(new_word)
print(checksum)
print(bola := '0x02' + new_word + '0x03' + str(checksum))
