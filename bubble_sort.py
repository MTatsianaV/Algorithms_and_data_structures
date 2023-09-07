import random

# Создаем массив из 10 случайных элементов от 0 до 100
array = [random.randint(0, 100) for _ in range(10)]
print("Исходный массив:", array)

# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(array)
print("Пузырьковая сортировка:", array)