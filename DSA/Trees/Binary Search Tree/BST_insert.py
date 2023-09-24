class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        New_Node = Node(value)
        if self.root == None:
            self.root = New_Node
            return True
        temp = self.root
        while True:
            if New_Node.value == temp.value:
                return False
            elif New_Node.value < temp.value:
                if temp.left == None:
                    temp.left = New_Node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = New_Node
                    return True
                temp = temp.right


a = Binary_Search_Tree()
a.insert(2)
a.insert(1)
a.insert(3)
print(a.root.value)
print(a.root.left.value)
print(a.root.right.value)
