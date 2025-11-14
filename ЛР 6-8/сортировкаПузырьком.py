def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже отсортированы,
        # их можно исключить из перебора
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Отсортированный массив:", array)
