#Height of a Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

def height(node):
    if node is None:
        return -1               # by definition: leaf height = 0
    return 1 + max(height(node.left), height(node.right))

  
n = int(input().strip())
values = list(map(int, input().split()))
root = None
for v in values:
root = insert_bst(root, v)
print(height(root))


#Mirror Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def attach(parent_map, child_map, u, v, side):
    if u not in parent_map:
        parent_map[u] = Node(u)
    if v not in parent_map:
        parent_map[v] = Node(v)
    if side == 'L':
        parent_map[u].left = parent_map[v]
    else:
        parent_map[u].right = parent_map[v]
    child_map.add(v)

def build_tree(n):
    nodes = {}
    children = set()
    for _ in range(n - 1):
        u, v, c = input().split()
        attach(nodes, children, int(u), int(v), c)
    # root is the one never mentioned as child
    root_key = (set(nodes) - children).pop()
    return nodes[root_key]

def are_mirrors(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None or a.key != b.key:
        return False
    return are_mirrors(a.left, b.right) and are_mirrors(a.right, b.left)


n = int(input().strip())
root1 = build_tree(n)
root2 = build_tree(n)
print("yes" if are_mirrors(root1, root2) else "no")



