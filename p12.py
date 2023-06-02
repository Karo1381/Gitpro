class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def connect(self, other_list):
        if self.head is None:
            self.head = other_list.head
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = other_list.head

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)

linked_list2 = LinkedList()
linked_list2.append(4)
linked_list2.append(5)
linked_list2.append(6)

linked_list1.connect(linked_list2)
linked_list1.print_list()
