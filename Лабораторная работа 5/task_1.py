from pprint import pprint

first_number = 0  # первое число в списке словарей
last_number = 15  # последнее число в списке словарей


def numbers_dict(number: int) -> dict:  # создаем словарь с числами в различных системах счисления
    dict_ = {
        'bin': bin(number),
        'dec': number,
        'hex': hex(number),
        'oct': oct(number)
    }
    return dict_


dicts_list = [numbers_dict(number) for number in range(first_number, last_number + 1)]  # создаем список словарей

pprint(dicts_list)

