from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    
def create_binary_tree(arr, index):

    if index < len(arr):
        root = TreeNode(arr[index])
        root.left = create_binary_tree(arr, index * 2 + 1)
        root.right = create_binary_tree(arr, index * 2 + 2)
        return root
    return None

def print_binary_tree(root, prefix="", is_left=True):
    if not root:
        print("Empty Tree")
        return

    if root.right:
        print_binary_tree(root.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))

    if root.left:
        print_binary_tree(root.left, prefix + ("    " if is_left else "│   "), True)

def printNode_pre_order(root):
    if root:
        print(root.val)
        printNode_pre_order(root.left)
        printNode_pre_order(root.right)

def insert(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if root.val > val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root


def in_order_traversal_to_arr(root: Optional[TreeNode]):
    my_list = []
    in_order(root,my_list)
    return my_list

def in_order(root,my_list):
    if root:
        if root.val:
            my_list.append(root.val)
        in_order(root.left,my_list)
        in_order(root.right,my_list)

def bfsTraversalToArray(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = create_binary_tree(arr,0)
    print("BFS Traversal of Binary Tree:")
    print_binary_tree(root)

    print(bfsTraversalToArray(root))
    # test(root)