from ast import literal_eval


word = str.encode(input('digita ai: '))
new_word = ''
checksum = 0
array = bytearray()


for i in word:
    if not array:
        array.append(result := literal_eval(hex(2)))
    
    checksum ^= literal_eval(hex(i))
    array.append(result := literal_eval(hex(i)))
    new_word += hex(i)
    print(hex(i), '\n')


array.append(result := literal_eval(hex(3)))
array.append(checksum)


#print(new_word)
#print(checksum)
#print(array)
print('-----')
print(array)
#print(bola := bytearray((('0x02' + new_word + '0x03' + str(checksum)).encode())))
conta = 0
for i in array:
    print(hex(i))
conta ^= literal_eval(hex(i))

# print(r := literal_eval(hex((str.encode('\3')))))