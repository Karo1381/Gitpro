class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return None
        else:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node.data

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, data):
        self.linked_list.insert_at_beginning(data)

    def pop(self):
        return self.linked_list.delete_at_beginning()

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop()) # Output: 3
print(stack.pop()) # Output: 2
print(stack.pop()) # Output: 1
print(stack.pop()) # Output: None
