class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        New_Node = Node(value)
        self.top = New_Node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        New_Node = Node(value)
        if self.height == 0:
            self.top = New_Node
            self.height = 1
        else:
            New_Node.next = self.top
            self.top = New_Node
        self.height += 1


a = Stack(3)
a.push(5)
a.push(6)
a.print_stack()
