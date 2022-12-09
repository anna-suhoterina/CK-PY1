from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n=8) -> str:
    possible_symbols_str = ascii_uppercase + ascii_lowercase + digits  # строка возможных символов
    password = "".join(sample(possible_symbols_str, n))
    return password


print(get_random_password())

