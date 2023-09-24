class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenth = 1


my_linked_list = Linked_List(2)

print(my_linked_list.head.value)
