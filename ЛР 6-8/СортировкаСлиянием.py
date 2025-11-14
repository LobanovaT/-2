def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        # Разделяем массив на две части
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем обе части
        merge_sort(left_half)
        merge_sort(right_half)

        # Индексы для перебора
        i = j = k = 0

        # Сливаем отсортированные части
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Если остались элементы в левой половине, добавляем их
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Если остались элементы в правой половине, добавляем их
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
merge_sort(array)
print("Отсортированный массив:", array)
