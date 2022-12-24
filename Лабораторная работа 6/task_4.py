import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as f:
        csv_table = f.read()  # считываем из исходного файла csv "таблицу" с данными

    rows_list = csv_table.split()  # формируем лист из строк таблицы
    dicts_list = [dict(zip(rows_list[0].split(','), row.split(','))) for row in rows_list[1:]]

    return dicts_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

