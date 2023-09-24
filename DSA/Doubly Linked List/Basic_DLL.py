class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.pre = None
        self.next = None


class DoublyLinkedList:
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
            New_Node.pre = self.tail
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        New_Node = Node(value)
        if self.length == 0:
            self.head - New_Node
            self.tail = New_Node
        else:
            New_Node.next = self.head
            self.head.pre = New_Node
            self.head = New_Node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            temp.pre = None
            temp.next = None
            self.tail = self.tail.pre
        self.length -= 1
        return temp.value

    def pop_first(s)


#    my_doubly_linked_list = DoublyLinkedList(3)
# my_doubly_linked_list.print_list()
my_doubly_linked_list = DoublyLinkedList(99)
my_doubly_linked_list.append(9)
my_doubly_linked_list.prepend(1)
my_doubly_linked_list.print_list()
print(my_doubly_linked_list.pop())
my_doubly_linked_list.pop()
print("\n")
my_doubly_linked_list.print_list()
