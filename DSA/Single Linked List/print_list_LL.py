class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


a = LinkedList(2)
a.print_list()
