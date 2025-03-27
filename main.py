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
        self.head = None
        self.tail = None

    def add_to_directory(self, parent, name, is_directory = True):
        new_node = Node(name, is_directory)
        return new_node
        
