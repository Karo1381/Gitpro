class Student:
    def __init__(self, name, number, average):
        self.name = name
        self.number = number
        self.average = average

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, number, average):
        new_student = Student(name, number, average)
        new_node = Node(new_student)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def find_by_name(self, name):
        current_node = self.head
        while current_node is not None:
            if current_node.data.name == name:
                return current_node.data.average
            current_node = current_node.next
        return None

linked_list = LinkedList()

for i in range(10):
    name = input("Enter name: ")
    number = input("Enter number: ")
    average = float(input("Enter average: "))
    linked_list.insert(name, number, average)

current_name = input("Enter a name to find average: ")
average = linked_list.find_by_name(current_name)

if average is not None:
    print(f"The average of {current_name} is {average}")
else:
    print("Student not found")
