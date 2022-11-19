class BinaryTree:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def add(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.add(data)
            else:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.add(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


tree = BinaryTree(10)
tree.add(12)
tree.add(124)
tree.add(122)
tree.print_tree()
