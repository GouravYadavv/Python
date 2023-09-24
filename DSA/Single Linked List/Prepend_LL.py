class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        New_Node = Node(value)
        self.head = New_Node
        self.tail = New_Node
        self.length = 1

    def prepend(self, value):
        New_Node = Node(value)
        if self.length == 0:
            self.head = New_Node
            self.tail = New_Node
        else:
            New_Node.next = self.head
            self.head = New_Node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


a = LinkedList(3)
a.prepend(4)
a.prepend(5)


a.print_list()
