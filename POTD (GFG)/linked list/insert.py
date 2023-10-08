class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head1, key):
        new_node = Node(key)
        
        if not head1:
            return new_node
        
        if key < head1.data:
            new_node.next = head1
            return new_node
        
        current = head1
        while current.next and current.next.data < key:
            current = current.next
        print(f"current is {current.data} going to be replaced by {new_node.data}")
        new_node.next = current.next
        current.next = new_node
        # print(f"new node next is {new_node.next.data}")
        # print(f"current next is {current.next.data} going to be replaced by {new_node.data} ")
        
        return head1

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Create a sample sorted linked list
head = Node(25)
head.next = Node(36)
head.next.next = Node(47)
head.next.next.next = Node(58)
head.next.next.next.next = Node(69)
head.next.next.next.next.next = Node(80)

# Create a Solution object
solution = Solution()

# Insert a new element into the sorted linked list
key = 75
head = solution.sortedInsert(head, key)

# Print the modified linked list
printLinkedList(head)

# # Test case 2: Insert 75 into the sorted linked list
# key = 75
# head = solution.sortedInsert(head, key)

# Print the modified linked list again
# printLinkedList(head)
