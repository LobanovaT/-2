def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # левый ребенок
    r = 2 * i + 2  # правый ребенок

    # Если левый потомок больше корня
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Если правый потомок больше текущего наибольшего
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами
        # Рекурсивно heapify для затронутой поддеревья
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        # текущий корень — наибольший элемент
        arr[0], arr[i] = arr[i], arr[0]  # перемещаем его в конец
        heapify(arr, i, 0)  # вызываем heapify для уменьшенного массива

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
heap_sort(array)
print("Отсортированный массив:", array)
