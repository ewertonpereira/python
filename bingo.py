from random import randint, shuffle
"""
adds numbers to the list according to the given range
(e.g.) -> min_rand: 1 | max_rand: 15 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
def add_numbers_list(min_rand: int, max_rand: int) -> list[int]:
    array:list[int] = []
    while min_rand <= max_rand:
        array.append(min_rand)
        min_rand += 1


    return array


b: list = add_numbers_list(1, 15)
i: list = add_numbers_list(16, 30)
n: list = add_numbers_list(31, 45)
g: list = add_numbers_list(46, 60)
o: list = add_numbers_list(61, 75)


# def bingo():

#     size_matrix:int = 5
#     matrix: list[list[int]] = []
    
#     for row in range(size_matrix):
#         list_row: list[int] = []
#         for column in range(size_matrix):



