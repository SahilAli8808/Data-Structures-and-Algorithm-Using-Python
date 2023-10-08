class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def pairWiseSwap(self, head):
        # Create a dummy node before the head to simplify edge cases
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        print(f"prev is {prev.data}")
        print(f"dummy is {dummy.data}")
        print(f"head is {head.data}")
        print(f"head next is {head.next.data}")
        # Swap nodes until there are no more nodes to swap

        while head and head.next:

            # Nodes to be swapped
            print(f"inside loop head is {head.data}")
            first = head
            print(f"here next data is  {head.next.data}")
            second = head.next
            # print(f"first is {first.data}")
            # print(f"second is {second.data}")
            # print(f"prev is {prev.data}")
            # print(f"prev next is {prev.next.data}")

            # Swap nodes
            print(f"now prevnode ke next {prev.next.data} ko second {second.data} se replace")
            prev.next = second
            print(f"now first next {first.next.data} ko second next {second.next} se replace")
            first.next = second.next
            print(f"second next {second.next} ko first {first.data} se replace")
            second.next = first

            # Update prev and head for the next iteration
            print(f"now prev is {first.data}")
            prev = first
            print(f"now head is {first.next}")

            head = first.next

        # Return the new head (skip the dummy node)
        print(f"dummy next is {dummy.next.data}")
        return dummy.next

# Helper function to print the linked list
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Test the code
if __name__ == "__main__":
    # Create a sample linked list
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    # Create a Solution object
    solution = Solution()

    # Swap the nodes pairwise
    new_head = solution.pairWiseSwap(head)

    # Print the modified linked list
    printLinkedList(new_head)
