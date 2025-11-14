def sequential_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Возвращает индекс найденного элемента
    return -1  # Если элемент не найден, возвращает -1

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
target_value = 22

index_found = sequential_search(array, target_value)
if index_found != -1:
    print(f"Элемент {target_value} найден на позиции {index_found}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")
