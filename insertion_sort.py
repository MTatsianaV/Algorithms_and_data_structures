import random

# Создаем массив из 10 случайных элементов от 0 до 100
array = [random.randint(0, 100) for _ in range(10)]
print("Исходный массив:", array)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

insertion_sort(array)
print("Сортировка вставками:", array)