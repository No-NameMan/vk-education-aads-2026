from collections import deque
import heapq


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.balance_factor = None


# 1. Проверка полноты бинарного дерева.
# BFS посещает позиции по уровням слева направо.
# После первого пропуска все последующие позиции должны быть пустыми.
# Время O(n), память O(w), где w - максимальная ширина дерева.
def is_complete(root):
    queue = deque([root])
    seen_empty = False

    while queue:
        node = queue.popleft()

        if node is None:
            seen_empty = True
            continue

        if seen_empty:
            return False

        queue.append(node.left)
        queue.append(node.right)

    return True


# 2. Объединение K отсортированных массивов.
# В куче храним первый оставшийся элемент каждого непустого массива.
# Минимум кучи всегда является минимумом среди всех оставшихся элементов.
# Время O(K + N*log(K+1)), память O(K) без учета результата O(N).
# N - общее число элементов, K - число исходных массивов.
def merge_sorted_arrays(arrays):
    heap = []

    for array_index, array in enumerate(arrays):
        if array:
            heap.append((array[0], array_index, 0))

    heapq.heapify(heap)
    result = []

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        result.append(value)

        next_index = element_index + 1
        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heapq.heappush(heap, (next_value, array_index, next_index))

    return result


# 3. K-й наименьший и K-й наибольший элементы массива.
# Нумерация начинается с 1. Повторяющиеся значения учитываются отдельно.
# Для K-го наименьшего храним K минимальных значений в max-heap.
# В heapq используем противоположные знаки, чтобы получить max-heap.
# Корень хранит наибольшее среди K отобранных значений.
# Время O(n*log(K+1)), память O(K).
def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None

    heap = [-value for value in arr[:k]]
    heapq.heapify(heap)

    for value in arr[k:]:
        if -value > heap[0]:
            heapq.heapreplace(heap, -value)

    return -heap[0]


# Для K-го наибольшего храним K максимальных значений в min-heap.
# Корень кучи - наименьшее среди них, то есть искомый K-й элемент.
# Время O(n*log(K+1)), память O(K).
def kth_largest(arr, k):
    if k < 1 or k > len(arr):
        return None

    heap = arr[:k]
    heapq.heapify(heap)

    for value in arr[k:]:
        if value > heap[0]:
            heapq.heapreplace(heap, value)

    return heap[0]


# 4. K-й наименьший или наибольший элемент BST.
# Inorder обходит BST по возрастанию, обратный inorder - по убыванию.
# Завершаем обход сразу после посещения K-го узла.
# Время O(h+K), память O(h), h - высота дерева в узлах.
def kth_bst(root, k, largest=False):
    if k < 1:
        return None

    stack = []
    current = root
    count = 0

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.right if largest else current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.value

        current = current.left if largest else current.right

    return None


def kth_smallest_bst(root, k):
    return kth_bst(root, k)


def kth_largest_bst(root, k):
    return kth_bst(root, k, largest=True)


# 5. Вычисление коэффициента баланса каждого узла.
# Используем соглашение семинара: высота слева минус высота справа.
# DFS снизу вверх возвращает высоты поддеревьев, не пересчитывая их.
# Высота пустого дерева 0, высота листа 1.
# Время O(n), память O(h) на стек рекурсии.
def fill_balance_factors(root):
    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)
        node.balance_factor = left_height - right_height

        return 1 + max(left_height, right_height)

    height(root)
    return root


# 6. Зеркальное отражение бинарного дерева.
# В каждом узле меняем местами потомков и зеркально отражаем поддеревья.
# По рекурсии получаем зеркальную структуру всего дерева.
# Время O(n), память O(h) на стек рекурсии.
def mirror_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root
