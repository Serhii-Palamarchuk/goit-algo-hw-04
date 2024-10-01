# goit-algo-hw-04
Домашнє завдання до теми “Алгоритми сортування”

## Опис

У цьому проекті було проведено порівняльний аналіз трьох алгоритмів сортування: сортування злиттям, сортування вставками та Timsort (вбудована функція `sorted` в Python). Метою було емпірично перевірити їхню теоретичну складність і показати, що поєднання сортування злиттям і сортування вставками в алгоритмі Timsort робить його значно ефективнішим.

### Алгоритми:
1. **Сортування злиттям (Merge Sort)**: O(n log n)
2. **Сортування вставками (Insertion Sort)**: O(n²)
3. **Timsort (вбудована функція `sorted`)**: O(n log n), але використовує сортування вставками для малих підмасивів.

## Порівняння продуктивності

Алгоритми були протестовані на масивах різних розмірів з випадковими даними. Час виконання було виміряно за допомогою модуля `timeit`. Ось приклад результатів тестування:

| Розмір масиву | Merge Sort (сек) | Insertion Sort (сек) | Timsort (сек) |
| ------------- | ---------------- | -------------------- | ------------- |
| 100           | 0.00245          | 0.00185              | 0.00045       |
| 1000          | 0.02078          | 0.28123              | 0.00125       |
| 5000          | 0.12467          | 7.35254              | 0.00734       |

Як видно з таблиці, сортування вставками показує гірші результати на великих наборах даних, тоді як Timsort працює швидше за рахунок використання сортування вставками для малих підмасивів, що покращує загальну ефективність.

## Висновки

1. **Timsort** значно ефективніший на великих наборах даних завдяки використанню сортування вставками для малих підмасивів і сортування злиттям для великих.
2. **Сортування вставками** може бути ефективним для малих масивів, але на великих наборах даних його продуктивність значно гірша, що підтверджується теоретичною складністю O(n²).
3. **Сортування злиттям** забезпечує стабільну продуктивність O(n log n), але Timsort оптимізує цей процес завдяки використанню сортування вставками.

Таким чином, програмісти зазвичай використовують вбудовані в Python алгоритми сортування (Timsort), а не кодують сортування з нуля через їхню ефективність і простоту у використанні.

## Необов'язкове завдання: Злиття k відсортованих списків

Реалізована функція `merge_k_lists`, яка об'єднує кілька відсортованих списків у один. Приклад:

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
