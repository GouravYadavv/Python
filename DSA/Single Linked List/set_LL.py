class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        New_Node = Node(value)
        self.head = New_Node
        self.tail = New_Node
        self.length = 1

    def get(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def append(self, value):
        New_Node = Node(value)
        if self.length == 0:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1

    def set(self, index, value):
        temp = self.get(index)
        if (
            temp
        ):  # It is a short form of if temp is not None, means if temp contains some value.
            temp.value = value
        return False

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.append(9)
my_linked_list.print_list()
my_linked_list.set(2, 99)
my_linked_list.print_list()
