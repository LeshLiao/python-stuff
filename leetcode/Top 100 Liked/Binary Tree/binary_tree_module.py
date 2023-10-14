from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def array_to_binary_tree(arr):
    if not arr:
        return None

    # Create a queue to hold the nodes as we build the tree
    queue = []

    # Create the root node from the first element of the array
    root = TreeNode(arr[0])
    queue.append(root)

    i = 1  # Start with the second element in the array

    while i < len(arr):
        current_node = queue.pop(0)

        # Create the left child node
        if i < len(arr):
            if arr[i] is not None:
                current_node.left = TreeNode(arr[i])
                queue.append(current_node.left)
            i += 1

        # Create the right child node
        if i < len(arr):
            if arr[i] is not None:
                current_node.right = TreeNode(arr[i])
                queue.append(current_node.right)
            i += 1

    return root


def binary_tree_to_array(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)

        if current_node:
            result.append(current_node.val)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            result.append(None)

    # Trim any trailing None values from the list
    while result and result[-1] is None:
        result.pop()

    return result

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = array_to_binary_tree(arr)
    print("BFS Traversal of Binary Tree:")
    print_binary_tree(root)

    print(binary_tree_to_array(root))
    # test(root)