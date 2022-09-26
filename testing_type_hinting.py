def ceasar(text: str, key: int) -> str:
    result: str = ''
    for char in text:
        c: int = ord(char)
        enc_char: str = chr(c + key)
        result += enc_char
    return result


#print(result := (ceasar('golden ball', 2)))


from ast import Tuple
from typing import Any, Optional

def print_twice(something: Any) -> None:
    print(something, something, "!")


print_twice('bola')

# ------------------------------------
from typing import Union

def print_thing(thing: Union[str, int]) -> None:
    if isinstance(thing, str):
        print('String:', thing + '!')
    else:
        print('Number:', thing + 10)


print_thing(1)
print_thing('d')


# -------------------------------

# def print_salary_entry(entry: Tuple[str, Optional[int]]) -> None:
#     name, salary = entry
#     if salary is None:
#         print(f"{name} is a volunteer")
#     else:
#         print(f"Salary of {name}: {salary}")


# print_salary_entry(('jose',88))
