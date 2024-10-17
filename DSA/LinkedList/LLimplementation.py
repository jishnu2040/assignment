class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def Print_list(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data, end=" ->")
                n = n.ref

    def add_node(self, data):
        new_node = Node(data)

        if self.head is  None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def remove_node(self,data):

        if self.head is None:
            print("linked list is empty!")
            return
        if self.head.data == data:
            self.head = self.head.ref
            print("data removed !")
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == data:
                n.ref = n.ref.ref
                print("node deleted")
            
            n = n.ref
        print("node data not founded!")



linkedD = LinkedList()


linkedD.add_node(12)
linkedD.add_node(23)
linkedD.add_node(45)

# Print the linked list
print("Linked List Before Removal:")
linkedD.Print_list()


linkedD.remove_node(23)

linkedD.Print_list()