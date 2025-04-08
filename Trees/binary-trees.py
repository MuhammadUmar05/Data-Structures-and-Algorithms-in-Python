import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class TreeBuilder:
    index = -1

    @staticmethod
    def buildTree(arr):
        TreeBuilder.index += 1
        if arr[TreeBuilder.index] == -1:
            return None
        root = Node(arr[TreeBuilder.index])
        root.left = TreeBuilder.buildTree(arr)
        root.right = TreeBuilder.buildTree(arr)
        return root


# Depth First Search DFS
def inorder(root):  # left root right
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def postorder(root):  # left right root
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def preorder(root):  # root left right
    if not root:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Breadth First Search BFS
def levelOrderTraversal(root):
    q = queue.Queue()
    if not root:
        return
    q.put(root)
    while not q.empty():
        curr = q.get()
        print(curr.data, end=" ")
        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)


arr = [1, 2, 3, -1, -1, 4, -1, -1, 5, 6, -1, -1, -1]
root = TreeBuilder.buildTree(arr)
print("Inorder Traversal: ", end="")
inorder(root)
print("\nPostorder Traversal: ", end="")
postorder(root)
print("\nPreorder Traversal: ", end="")
preorder(root)
print("\nLevel order Traversal: ", end="")
levelOrderTraversal(root)
