class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        New_node = Node(value)
        self.head = New_node
        self.tail = New_node
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

    def Pop_First(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp


a = LinkedList(3)
a.append(2)
print(a.Pop_First())
print(a.Pop_First())
print(a.Pop_First())
