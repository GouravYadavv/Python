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
        else:
            New_Node.next = self.top
            self.top = New_Node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return f"Invalid index"
        elif self.height == 1:
            temp = self.top
            self.top = None
            self.height = 0
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height -= 1
        return temp.value  # Returning temp.value to return the value.


a = Stack(2)

a.push(3)
a.push(5)
a.print_stack()
print(a.pop())
print(a.pop(), "\n")
a.print_stack()  # Only element 2 left in the stack rest are already being poped.
