def fibonachi_search(arr, target):
    # Генерируем последовательность Фибоначчи, не превышающую длину массива
    fibs = [0, 1]
    while fibs[-1] < len(arr):
        fibs.append(fibs[-1] + fibs[-2])

    # Инициализация индексов
    offset = -1
    fib_idx = len(fibs) - 1

    while fib_idx > 1:
        # Вычисляем индекс для сравнения
        i = min(offset + fibs[fib_idx - 2], len(arr) - 1)
        if arr[i] == target:
            return i
        elif arr[i] < target:
            fib_idx -= 1
            offset = i
        else:
            fib_idx -= 2
    # Проверка последнего возможного элемента
    if fibs[fib_idx - 1] and offset + 1 < len(arr) and arr[offset + 1] == target:
        return offset + 1
    return -1

# Пример использования
array = [10, 22, 35, 40, 45, 50, 60]
target_value = 40
index = fibonachi_search(array, target_value)
print("Индекс элемента:", index)
