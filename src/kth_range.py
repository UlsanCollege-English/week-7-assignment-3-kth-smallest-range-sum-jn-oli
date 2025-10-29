class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    """Insert into BST — duplicates are ignored."""
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def kth_smallest(root, k):
    """Return the kth smallest value (1-based). Raises IndexError if k too large."""
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val

        cur = cur.right

    raise IndexError("k is too large for the tree")


def range_sum_bst(root, low, high):
    """Sum nodes within inclusive range [low, high] using BST pruning."""
    if not root:
        return 0

    total = 0
    if root.val > low:
        total += range_sum_bst(root.left, low, high)
    if low <= root.val <= high:
        total += root.val
    if root.val < high:
        total += range_sum_bst(root.right, low, high)

    return total
