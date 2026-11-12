from collections import deque


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 1. Восстановление дерева из массива
# Массив хранит узлы по позициям: корень - 0, потомки - 2*i+1 и 2*i+2.
# None обозначает отсутствие узла. Рекурсия строит оба поддерева.
# Время O(n), память O(n) на узлы и O(log(n+1)) на стек.
def build_tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None

    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    return root


# 2. Проверка симметричности
# Сравниваем зеркальные пары: левый узел с правым и наоборот.
# Два пустых узла совпадают, различие значений или структуры дает False.
# Время O(n), память O(h) на стек рекурсии.
def is_symmetric(root):
    def mirror(a, b):
        if a is None or b is None:
            return a is b

        return (
            a.data == b.data
            and mirror(a.left, b.right)
            and mirror(a.right, b.left)
        )

    if root is None:
        return True

    return mirror(root.left, root.right)


# 3. Минимальная глубина
# BFS обходит дерево по уровням, поэтому первый найденный лист ближайший.
# Глубину считаем в узлах: корень имеет глубину 1.
# Время O(n), память O(w), где w - максимальная ширина дерева.
def min_depth(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        if node.left is None and node.right is None:
            return depth

        if node.left is not None:
            queue.append((node.left, depth + 1))

        if node.right is not None:
            queue.append((node.right, depth + 1))


# 4. Произведение минимума и максимума BST
# По свойству BST минимум находится на крайнем левом пути,
# а максимум - на крайнем правом. Строить дерево не требуется.
# Массив задан позиционно, как в задаче 1.
# Время O(h), память O(1), где h - высота дерева.
def min_max_product(arr):
    if not arr or arr[0] is None:
        return None

    left = right = 0
    n = len(arr)

    while 2 * left + 1 < n and arr[2 * left + 1] is not None:
        left = 2 * left + 1

    while 2 * right + 2 < n and arr[2 * right + 2] is not None:
        right = 2 * right + 2

    return arr[left] * arr[right]


# 5. Сравнение двух деревьев
# Деревья равны, когда совпадают значения и структура всех поддеревьев.
# Рекурсивно сравниваем соответствующих левых и правых потомков.
# Время O(n), память O(h) на стек рекурсии.
def is_same_tree(a, b):
    if a is None or b is None:
        return a is b

    return (
        a.data == b.data
        and is_same_tree(a.left, b.left)
        and is_same_tree(a.right, b.right)
    )
