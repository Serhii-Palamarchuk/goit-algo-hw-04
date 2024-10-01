# Необов'язкове завдання
# Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. 
# При виконанні завдання можете опиратися на алгоритм сортування злиттям з конспекту. 
# Реалізуйте функцію merge_k_lists , яка приймає на вхід список відсортованих списків та повертає відсортований список.

import heapq

def merge_k_lists(lists):
    merged_list = []
    heapq.heapify(merged_list)  # створюємо купу

    for lst in lists:
        for num in lst:
            heapq.heappush(merged_list, num)  # додаємо елементи до купи

    sorted_list = []
    while merged_list:
        sorted_list.append(heapq.heappop(merged_list))  # видаляємо найменші елементи по черзі

    return sorted_list

# Приклад
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
