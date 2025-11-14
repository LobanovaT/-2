def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Выбираем опорный элемент — обычно последний элемент
        pivot = arr[len(arr) // 2]
        # Разделяем массив по опорному элементу
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Рекурсивно сортируем подмассивы
        return quick_sort(left) + middle + quick_sort(right)

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = quick_sort(array)
print("Отсортированный массив:", sorted_array)
