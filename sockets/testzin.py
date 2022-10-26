import hashlib

file_name = 'horse_car.jpg'
hasher = hashlib.md5()

with open(file_name, 'rb') as file:
    content = file.read()
    hasher.update(content)
print(hasher.hexdigest())
