# Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний алгоритм сортування, 
# що поєднує в собі сортування злиттям і сортування вставками.
# Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання

import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Тестування алгоритмів
def test_sorts():
    sizes = [100, 1000, 5000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()

        print(f"\nРозмір масиву: {size}")

        # Тест сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(arr_copy1), number=1)
        print(f"Час виконання Merge Sort: {merge_time:.5f} сек")

        # Тест сортування вставками
        insert_time = timeit.timeit(lambda: insertion_sort(arr_copy2), number=1)
        print(f"Час виконання Insertion Sort: {insert_time:.5f} сек")

        # Тест Timsort (sorted)
        timsort_time = timeit.timeit(lambda: sorted(arr), number=1)
        print(f"Час виконання Timsort (sorted): {timsort_time:.5f} сек")

test_sorts()
