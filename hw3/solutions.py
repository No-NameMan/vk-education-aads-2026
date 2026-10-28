from collections import Counter


# 1. Корень числа. O(log(n + 1)) времени, O(1) памяти.
# Бинарный поиск последнего x, для которого x * x <= n.
def integer_sqrt(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным")

    left, right = 0, n + 1

    while left + 1 < right:
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid
        else:
            right = mid

    return left


# 2. Ксероксы. Бинарный поиск минимального подходящего времени.
# Первую копию делает быстрый ксерокс, затем работают оба.
def copy_time(n, x, y):
    if n <= 0:
        return 0

    first = min(x, y)
    left, right = 0, (n - 1) * first

    while left < right:
        mid = (left + right) // 2
        if mid // x + mid // y >= n - 1:
            right = mid
        else:
            left = mid + 1

    return first + left


# 3. Животные. O(n log n + m log m) времени.
# Каждую порцию отдаем самому неприхотливому оставшемуся животному.
def feed_animals(animals, food):
    animals = sorted(animals)
    food = sorted(food)
    count = 0

    for portion in food:
        if count == len(animals):
            break
        if portion >= animals[count]:
            count += 1

    return count


# 4. Лишняя буква. O(len(a) + len(b)) времени в среднем.
# Подсчитываем символы a и вычитаем их при обходе b.
def extra_letter(a, b):
    counts = {}

    for char in a:
        counts[char] = counts.get(char, 0) + 1

    for char in b:
        if counts.get(char, 0) == 0:
            return char
        counts[char] -= 1

    return ""


# 5. Сумма двух чисел. O(n) времени и памяти в среднем.
# Ищем дополнение среди уже просмотренных элементов.
def two_sum(nums, target):
    seen = {}

    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i

    return []


# 6. Анаграммы. O(S) времени и памяти в среднем.
# Ключ группы задается частотами символов, S - общая длина строк.
def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = frozenset(Counter(word).items())
        groups.setdefault(key, []).append(word)

    return list(groups.values())
