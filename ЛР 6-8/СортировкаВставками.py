def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые больше ключа, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # вставляем ключ на его правильную позицию
        arr[j + 1] = key

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(array)
print("Отсортированный массив:", array)
