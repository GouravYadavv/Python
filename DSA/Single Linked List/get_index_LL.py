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
        if self.head is None:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1

    def get(self, index):
        if index < 0 or self.length <= index:
            return "ValueError: Unsufficient Value"
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value


my_linked_list = LinkedList(2)
my_linked_list.append(7)
my_linked_list.append(4)
my_linked_list.append(9)
print(my_linked_list.get(2))
