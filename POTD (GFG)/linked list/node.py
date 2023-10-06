# to learn linked list ... first step is to learn to create a node 
"""
toh pahla kaam ye hota hai ki aap ak node banaye jo ak bluprint hoga sb elements ke liye 
yani blueprint se ye smjh me ata hai ki hame class banani hogi 
aur wo class collection hoga data aur ak reference (nextNode)
"""
class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None
        print(f"element added {self.data}")
"""
node ban gya aur isme jo value aayegi uske liye ak node ban jayega
ab next kaam hai uska object banana kyuki kisi bhi class ka instance hota hai object aur whi class ko use 
krta hai 
"""
firstNode = Node(1)
secondNode = Node(2)
"""
object ban gya  
"""
firstNode.nextNode = secondNode

current_node = firstNode
while current_node:
    print(current_node.data)
    current_node = current_node.nextNode
