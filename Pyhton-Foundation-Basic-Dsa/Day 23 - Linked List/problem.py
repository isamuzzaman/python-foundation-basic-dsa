class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #  Insert at Beginning
    def insert_front(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    #  Insert After a Given Node (Middle)
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be None")
            return

        temp = Node(data)
        temp.next = prev_node.next
        prev_node.next = temp

    #  Insert at Last
    def insert_last(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = temp

    # Print List
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Search 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Search Function
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return "Found"
            temp = temp.next

        return "Not Found"
    class Node:
     def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Reverse Function
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   
            current.next = prev       
            prev = current            
            current = next_node       

        self.head = prev

# Delete Function
def delete(self, key):
    temp = self.head

    # If head needs to be deleted
    if temp is not None:
        if temp.data == key:
            self.head = temp.next
            temp = None
            return

    # Search for the key
    prev = None
    while temp is not None:
        if temp.data == key:
            break
        prev = temp
        temp = temp.next

    # If key not found
    if temp is None:
        print(f"{key} not found in the list")
        return

    # Unlink node
    prev.next = temp.next
    temp = None