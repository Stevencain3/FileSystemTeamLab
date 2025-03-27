# Node represents a file or directory
class Node:
    def __init__(self, name, is_directory=True):
        self.name = name
        self.is_directory = is_directory
        self.content = "" if not is_directory else None
        self.children = [] if is_directory else None
        self.prev = None
        self.next = None


#set up a dubble linked list to have the file structure I want
class DoubleLinkedList:
    def __init__(self):
        self.head = None # keeps track of the first node 
        self.tail = None # Keeps track of the last node


    # creates a new file or folder 
    def add_node(self, name, is_directory=True):
        new_node = Node(name, is_directory)
        if not self.head: # if empty then this new node becomes both the tail and head
            self.head = self.tail = new_node
        else: # else if not empty then it puts it at the end and connects it back to the one before it
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    

    def add_to_directory(self, parent, name, is_directory = True):
        new_node = Node(name, is_directory)
        return new_node
        
