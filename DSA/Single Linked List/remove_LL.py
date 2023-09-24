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
        if self.length == 0:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1

    def get(self, index):
        if index < 0 or index > self.length:
            return "IndexError: Insufficient index."
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    def remove(self, index):
        if index < 0 or index > self.length:
            return "IndexError: Unsufficient indec"
        else:
            pre = self.get(index - 1)
            temp = self.get(index)
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp.value


my_linked_liist = LinkedList(3)
my_linked_liist.append(5)
my_linked_liist.append(1)
my_linked_liist.append(9)
print("Previous List:", end=" ")
my_linked_liist.print_list()
print("\n Element Removed:", my_linked_liist.remove(2))
print("New List:", end=" ")
my_linked_liist.print_list()
