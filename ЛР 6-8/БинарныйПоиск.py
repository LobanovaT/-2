def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Элемент найден, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой части
        else:
            right = mid - 1  # Ищем в левой части
    return -1  # Элемент не найден

# Пример использования
array = [11, 12, 22, 25, 34, 64, 90]
target_value = 22

index_found = binary_search(array, target_value)
if index_found != -1:
    print(f"Элемент {target_value} найден на позиции {index_found}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")
