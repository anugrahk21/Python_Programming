class Node:
    def __init__(self, data):
        # Constructor to initialize node with data and next as None
        self.data = data
        self.next = None

def insertatHead(head, tail, data):
    # Inserting a node at the head (beginning) of the list
    newNode = Node(data)
    if head is None:  # If the list is empty
        head = newNode
        tail = newNode
        return head, tail
    newNode.next = head  # Link the new node to the current head
    head = newNode       # Move the head to the new node
    return head, tail

def insertatEnd(head, tail, data):
    # Inserting a node at the tail (end) of the list
    newNode = Node(data)
    if head is None:  # If the list is empty
        head = newNode
        tail = newNode
        return head, tail
    tail.next = newNode  # Link the current tail to the new node
    tail = newNode       # Move the tail to the new node
    return head, tail

def insertatMid(head, tail, position, data):
    # Inserting a node at a given position (middle) of the list
    if position == 1:  # If position is 1, insert at the head
        return insertatHead(head, tail, data)
    
    temp = head
    p = 1
    while p < position - 1:  # Why position -1: Go to the node before the target position
        temp = temp.next  # Traverse the list until reaching the target position
        p += 1
    
    # If we enter the last position (e.g., if the length is 5 and we entered position 6)
    if temp.next is None:
        return insertatEnd(head, tail, data)
    
    newNode = Node(data)
    newNode.next = temp.next  # Link new node to the next node in the list
    temp.next = newNode       # Link the current node to the new node
    return head, tail

def deleteAtStart(head, pos):
    # Delete function (placeholder) can be implemented similarly
    pass

def display(head):
    # Display the entire linked list
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def find(a, head):
    # Search for a specific element in the linked list
    temp = head
    tf = False
    while temp is not None:
        if temp.data == a:  # If the data matches the element
            tf = True
            return tf
        temp = temp.next
    return tf

# Main execution starts here
if __name__ == "__main__":
    head = None
    tail = None
    print("AT HEAD")
    for i in range(5):
        data = int(input())  # Input data to insert at the head
        head, tail = insertatHead(head, tail, data)
    
    print("AT TAIL")
    for i in range(5):
        data = int(input())  # Input data to insert at the tail
        head, tail = insertatEnd(head, tail, data)
    
    display(head)  # Display the linked list

    print("Position to insert: ", end="")
    position = int(input())
    head, tail = insertatMid(head, tail, position, 200)  # Insert at a specific position
    display(head)  # Display the updated linked list

    print(head.data)  # Display head data
    print(tail.data)  # Display tail data

    print("Element to search: ", end="")
    a = int(input())  # Input the element to search in the list
    if find(a, head):
        print("Present")
    else:
        print("Not present")
