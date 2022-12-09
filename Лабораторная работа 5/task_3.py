from random import randint

start = -10  # первое число в диапазоне
stop = 10  # последнее число в диапазоне
count = 15  # количество чисел в списке


def get_unique_list_numbers() -> list[int]:
    random_numbers_list = []  # создаем пустой список для заполнения случайными числами
    while len(random_numbers_list) != count:  # пока количество чисел в списке не равно заданному количеству
        new_number = randint(start, stop)  # генерируем случайное целое число из заданного диапазона
        if new_number not in random_numbers_list:  # если этого числа еще нет в списке
            random_numbers_list.append(new_number)  # добавляем число в список
    return random_numbers_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
print(len(list_unique_numbers) == 15)

