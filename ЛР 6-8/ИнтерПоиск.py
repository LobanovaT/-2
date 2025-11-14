def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Предполагаемый индекс искомого элемента с помощью интерполяции
        mid = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Пример
array = [10, 20, 30, 40, 50, 60, 70]
target_value = 40
index = interpolation_search(array, target_value)
print("Индекс элемента:", index)
