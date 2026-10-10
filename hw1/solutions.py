"""VK Education: семинар 1 — фундаментальные задачи по массивам.

Все решения написаны на Python 3.9+ без сторонних библиотек.
Индексы в задачах считаются с нуля.
"""


# 1. Сумма чисел от 1 до n

def sum_from_1_to_n(n: int) -> int:
    """Вернуть 1 + 2 + ... + n. Время O(1), память O(1)."""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    return n * (n + 1) // 2


# 2. Two Sum в отсортированном массиве

def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Вернуть индексы пары с заданной суммой или []. O(n) / O(1)."""
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# 3. Разворот массива без дополнительных аллокаций

def reverse_array(nums: list[int]) -> list[int]:
    """Развернуть исходный массив. O(n) / O(1)."""
    _reverse_range(nums, 0, len(nums) - 1)
    return nums


def _reverse_range(nums: list[int], left: int, right: int) -> None:
    """Развернуть отрезок [left, right] исходного массива."""
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# 4. Циклический сдвиг массива вправо на k позиций

def rotate_right(nums: list[int], k: int) -> list[int]:
    """Выполнить сдвиг через три разворота. O(n) / O(1)."""
    n = len(nums)
    if n == 0:
        return nums

    k %= n
    _reverse_range(nums, 0, n - 1)
    _reverse_range(nums, 0, k - 1)
    _reverse_range(nums, k, n - 1)
    return nums


# 5. Слияние двух отсортированных массивов (с новым массивом)

def merge_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    """Вернуть отсортированное слияние. O(n + m) / O(n + m)."""
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


# 6. Слияние отсортированных массивов без дополнительного массива

def merge_sorted_in_place(nums1: list[int], nums2: list[int]) -> list[int]:
    """Слить массивы в nums1, заполняя его справа налево.

    Предполагается, что nums1 содержит сначала m отсортированных значений,
    а затем len(nums2) резервных ячеек (обычно нулей).
    Время O(m + n), дополнительная память O(1).
    """
    m = len(nums1) - len(nums2)
    i = m - 1
    j = len(nums2) - 1
    write = len(nums1) - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1

    return nums1


# 7. Минимальная длина подмассива с суммой >= target

def min_subarray_len(nums: list[int], target: int) -> int:
    """Для положительных nums вернуть минимальную длину или 0.

    Скользящее окно: время O(n), память O(1).
    """
    left = 0
    current_sum = 0
    min_len = len(nums) + 1

    for right, value in enumerate(nums):
        current_sum += value
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == len(nums) + 1 else min_len


# 8. Сортировка массива из 0 и 1

def sort_binary_array(nums: list[int]) -> list[int]:
    """Переместить все нули в начало, единицы в конец. O(n) / O(1)."""
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] == 0:
            left += 1
        elif nums[right] == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


# 9. Задача флага Нидерландов: сортировка 0, 1, 2

def sort_colors(nums: list[int]) -> list[int]:
    """Разделить массив на области 0 / 1 / 2. O(n) / O(1)."""
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # По условию здесь обязательно 2.
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


# 10. Перемещение чётных чисел в начало

def even_first(nums: list[int]) -> list[int]:
    """Сохранить относительный порядок чётных чисел. O(n) / O(1).

    Относительный порядок нечётных чисел не гарантируется.
    """
    even_index = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[even_index] = nums[even_index], nums[i]
            even_index += 1

    return nums


# 11. Перемещение всех нулей в конец

def move_zeroes(nums: list[int]) -> list[int]:
    """Переместить нули в конец, сохранив порядок остальных. O(n) / O(1)."""
    write = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write], nums[i] = nums[i], nums[write]
            write += 1

    return nums


if __name__ == "__main__":
    # Примеры и простая проверка всех задач.
    assert sum_from_1_to_n(1_000_000) == 500_000_500_000
    assert two_sum_sorted([3, 8, 9, 11, 16, 18, 19, 21], 25) == [2, 4]
    assert reverse_array([3, 8, 6, 9, 9, 8, 6]) == [6, 8, 9, 9, 6, 8, 3]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert merge_sorted_arrays([3, 8, 10, 11], [1, 7, 9]) == [1, 3, 7, 8, 9, 10, 11]
    assert merge_sorted_in_place([3, 8, 10, 11, 0, 0, 0], [1, 7, 9]) == [1, 3, 7, 8, 9, 10, 11]
    assert min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2
    assert sort_binary_array([1, 0, 1, 1, 0, 0]) == [0, 0, 0, 1, 1, 1]
    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert even_first([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 1, 11, 3, 9]
    assert move_zeroes([0, 0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0, 0]
    print("Все примеры пройдены.")
