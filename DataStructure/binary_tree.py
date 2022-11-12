class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            if data < new_node.data:
                if new_node.left is None:
                    new_node.left = Node(data)
                else:
                    new_node.left.add(data)
            else:
                if new_node.right is None:
                    new_node.right = Node(data)
                else:
                    new_node.right.add(data)


tree = BinaryTree()

