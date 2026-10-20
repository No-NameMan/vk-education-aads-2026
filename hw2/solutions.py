"""VK Education: домашнее задание 2 — списки и метод двух указателей.

Все восемь задач решены на Python 3.9+ без сторонних библиотек.
Функции для списков принимают голову односвязного списка (ListNode или None).
Оценки сложности указаны в формате: время / дополнительная память.
"""

from typing import Optional


class ListNode:
    """Узел односвязного списка."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# 1. Разворот односвязного списка

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Развернуть список изменением ссылок. O(n) / O(1).

    Перед заменой current.next сохраняем следующий узел, чтобы
    не потерять ещё не обработанную часть списка.
    """
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# 2. Поиск середины списка

def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Найти середину за один проход. O(n) / O(1).

    Быстрый указатель делает два шага за итерацию, медленный — один.
    Для списка чётной длины возвращается вторая середина.
    """
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# 3. Удаление элементов из односвязного списка по значению

def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """Удалить все узлы со значением val без создания нового списка.

    Фиктивная голова упрощает удаление первого элемента.
    После удаления prev не двигаем: следующий узел тоже может подходить.
    O(n) / O(1).
    """
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next is not None:
        if prev.next.val == val:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next


# 4. Проверка, является ли a подпоследовательностью b

def is_subsequence(a: str, b: str) -> bool:
    """Проверить сохранение порядка символов a в b. O(len(b)) / O(1).

    Указатель i передвигается только при совпадении ожидаемого символа.
    Дополнительная очередь не требуется.
    """
    i = 0

    for char in b:
        if i < len(a) and a[i] == char:
            i += 1

    return i == len(a)


# 5. Two Sum в отсортированном массиве

def has_pair_with_sum(nums: list[int], target: int) -> bool:
    """Проверить существование пары разных элементов. O(n) / O(1).

    Если сумма мала, увеличиваем левый элемент; если велика — уменьшаем
    правый. Отсортированность позволяет исключать неподходящие пары.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return False


# 6. Проверка палиндрома двумя указателями

def is_palindrome(s: str) -> bool:
    """Сравнить симметричные символы строки. O(n) / O(1)."""
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# 7. Удаление дубликатов из отсортированного массива in-place

def remove_duplicates(nums: list[int]) -> int:
    """Удалить повторы из исходного списка, вернуть новую длину.

    write обозначает следующую позицию для уникального значения,
    read просматривает массив. Хвост с повторами удаляется на месте.
    O(n) / O(1).
    """
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    del nums[write:]
    return write


# 8. Слияние двух отсортированных односвязных списков

def merge_sorted_lists(
    a: Optional[ListNode], b: Optional[ListNode]
) -> Optional[ListNode]:
    """Слить списки, используя только существующие узлы. O(n+m) / O(1).

    tail всегда указывает на последний узел отсортированной части.
    На каждом шаге переносится ссылка на меньший текущий узел.
    """
    if a is None:
        return b
    if b is None:
        return a

    if a.val <= b.val:
        head = tail = a
        a = a.next
    else:
        head = tail = b
        b = b.next

    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a is not None else b
    return head


if __name__ == "__main__":
    def make_list(values: list[int]) -> Optional[ListNode]:
        head = None
        for value in reversed(values):
            head = ListNode(value, head)
        return head

    def as_list(head: Optional[ListNode]) -> list[int]:
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        return result

    assert as_list(reverse_list(make_list([1, 2, 3]))) == [3, 2, 1]
    assert reverse_list(None) is None
    assert middle_node(make_list([1, 2, 3, 4, 5])).val == 3
    assert middle_node(make_list([1, 2, 3, 4])).val == 3
    assert middle_node(None) is None
    assert as_list(remove_elements(make_list([1, 2, 2, 3]), 2)) == [1, 3]
    assert remove_elements(make_list([2, 2]), 2) is None
    assert is_subsequence("abd", "uabqd")
    assert not is_subsequence("abc", "acb")
    assert is_subsequence("", "abc")
    assert has_pair_with_sum([3, 8, 9, 11, 16], 25)
    assert not has_pair_with_sum([1, 2, 4], 8)
    assert not has_pair_with_sum([4], 8)
    assert is_palindrome("level")
    assert is_palindrome("")
    assert not is_palindrome("hello")
    nums = [1, 1, 2, 2, 3, 3]
    assert remove_duplicates(nums) == 3 and nums == [1, 2, 3]
    assert remove_duplicates([]) == 0
    assert as_list(merge_sorted_lists(
        make_list([3, 6, 8]), make_list([4, 7, 9, 11])
    )) == [3, 4, 6, 7, 8, 9, 11]
    assert as_list(merge_sorted_lists(None, make_list([1]))) == [1]
    print("Все примеры пройдены.")
