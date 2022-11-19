class Node:
    def __init__(self, data=None, next_node=None):
        self.next_node = next_node
        self.data = data


class Linkedlist:
    def __init__(self):
        self.head = None

    def front_insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def back_insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        i = self.head
        while i.next_node:
            i = i.next_node
        i.next_node = Node(data, None)

    def printlist(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        i = self.head
        while i:
            print(f"{i.data} ----> ", end="")
            i = i.next_node


mylist = Linkedlist()
mylist.front_insert(10)
mylist.back_insert(40)
mylist.front_insert(2)


mylist.printlist()

