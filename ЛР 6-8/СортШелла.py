def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальный масштаб (разрыв)

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Выполняем сортировку вставками с указанным разрывом
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Уменьшаем разрыв для следующей итерации

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
shell_sort(array)
print("Отсортированный массив:", array)
