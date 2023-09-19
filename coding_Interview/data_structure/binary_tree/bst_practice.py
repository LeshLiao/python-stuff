
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data > data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root


def printNode(root):
    if root:
        printNode(root.left)
        print(root.data)
        printNode(root.right)


if __name__ == '__main__':

    r = Node(5)
    r = insert(r, 3)
    r = insert(r, 1)
    r = insert(r, 9)

    printNode(r)
