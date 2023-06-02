class student:
    def_init_(self,name,numbers,avarage):
    self.name=name self.number=number
    self.avarage=avarage
    class node:
        def_init_(self,data=None)
        self.data=data
        self.next=none
        class linkedlist:
            def_init_(self):
            self.head=none
            def insert(self,name,number,avarage):
                new_student=student(name,number,avarage)
                new_node=node(new_student)
                if self.head is None:
                    new_node
                    else:
                    current_node=self.head
                    while
                        current_node.next is not None:
                        current_node=
                        current_node.next
                        current_node.next=new_node
                        def find_by_name(self,name):
                            current_node=self.head
                            while current_node is not None:
                                if current_node.data.name==name:
                                    return
                                current_node.data.avarage current_node=
                                current_node.next return None
                            linked_list = linkedlist()
                            for i in range(10):
                            name=input("Entername:")
                            number=input("Enter name:")
                            number=input("Enter number:")
                            avarage=float(input("enter avarage"))
                           linked_list.insert(name,number,avarage)
                       current_name=input("enter a name to find avarage:")
                avarage=linked_list.find_by_name(current_name)
                if avarage is not None:
                    print(f"the avarage of{current_name}is {avarage}")
                else:
                    print("student not found")