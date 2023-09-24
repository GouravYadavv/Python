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

    def append(self, value):
        New_Node = Node(value)
        if self.head is None:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1


a = LinkedList(2)
a.append(3)
a.print_list()
