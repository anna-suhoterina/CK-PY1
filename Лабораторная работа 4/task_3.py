def delete(list_, index=None):
    if index is None or index == -1:
        return list_[:-1]
    elif index == 0:
        return list_[index + 1:]
    else:  # если индекс - другое отрицательное или положительное число
        return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

