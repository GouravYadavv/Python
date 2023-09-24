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

    def append(self, value):
        New_Node = Node(value)
        if self.length == 0:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(4)
my_linked_list.append(9)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.print_list()
my_linked_list.reverse()
print("\n")
my_linked_list.print_list()
