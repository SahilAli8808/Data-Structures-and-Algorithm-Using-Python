class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None
        # print(f"element added {self.data}")

class Linkedlist:
    def __init__(self):
        self.head = None
        # print(self.head)

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        # print(f"New object created {new_node} for {data}")
        # print(f"here {not self.head} ")

        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        
        current = self.head
        print(f"previous node is {current.nextNode}")

        while current.nextNode:
            current = current.nextNode
        current.nextNode = new_node  # Set the new node as the next of the last node
        print(f"current node is {current.nextNode}")
        print(f"self head node is {self.head.data}")

    def display(self):
        current = self.head
        if not current:
            print("Linked List is empty.")
            return
        while current:
            if current.nextNode:
                print(current.data, end=" -> ")
            else:
                print(current.data, end=" -> None")
            current = current.nextNode
Linkedlist = Linkedlist()
Linkedlist.insert_at_end(1)
Linkedlist.insert_at_end(8)
Linkedlist.display()
    
        
