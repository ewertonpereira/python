# file = open(address, mood)
with  open('oi.txt', 'r', encoding='utf-8') as file: 
    content = file.read()
    print(content)


with open('booyah.txt', 'w', encoding='utf-8') as file:
    file.write('Oh yeah! Booyah son of a bitch!')


with open('booyah.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)