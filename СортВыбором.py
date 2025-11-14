def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # предполагаем, что текущий элемент - минимальный
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # меняем местами найденный минимальный элемент с первым элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# пример использования
array = [64, 25, 12, 22, 11]
selection_sort(array)
print("Отсортированный массив:", array)
