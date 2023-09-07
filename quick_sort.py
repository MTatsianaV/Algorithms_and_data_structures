import random

# Создаем массив из 10 случайных элементов от 0 до 100
array = [random.randint(0, 100) for _ in range(10)]
print("Исходный массив:", array)

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_array = quick_sort(array)
print("Быстрая сортировка:", sorted_array)