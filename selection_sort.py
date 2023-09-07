import random

# Создаем массив из 10 случайных элементов от 0 до 100
array = [random.randint(0, 100) for _ in range(10)]
print("Исходный массив:", array)

# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(array)
print("Сортировка выбором:", array)