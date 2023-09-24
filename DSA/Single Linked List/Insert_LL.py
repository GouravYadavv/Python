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
        if index < 0 or index > self.length:
            return 0
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        New_Node = Node(value)
        if self.length == 0:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.head.next = self.head
            self.head = New_Node
        self.length += 1

    def insert(self, index, value):
        if index > self.length or index < 0:
            return "IndexError: Index Not Valid"
        elif index == self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        New_node = Node(value)
        temp = self.get(index - 1)
        New_node.next = temp.next
        temp.next = New_node
        self.length += 1


a = LinkedList(5)
a.append(3)
a.append(6)
a.insert(2, 9)
a.print_list()
print(a.get(2).value)
