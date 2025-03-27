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
    
 # creats new file/ folder but adds it into the folders children list
    def add_to_directory(self, parent, name, is_directory = True):
        new_node = Node(name, is_directory)
        parent.children.append(new_node)
        return new_node
        

# function for seting up the file sturcture for we dont have to make one up each time we run it
def setup_file_structure():
    fs = DoubleLinkedList()
    root = fs.add_node("Root")
    this_pc = fs.add_node("This PC")
    root.children = [this_pc]

    #testing
    current = fs.head
    while current:
        print(current.name)
        current = current.next

setup_file_structure()


# test cases for what I have so far
'''
# testing to see if its working the way I want it too
fs = DoubleLinkedList()
root_folder = fs.add_node("root", is_directory=True)
file1 = fs.add_node("readme.txt", is_directory=False)
folder1 = fs.add_node("Documents", is_directory=True)
docs = fs.add_to_directory(folder1, "Resume.docx", is_directory=False)
pics = fs.add_to_directory(folder1, "Photos", is_directory=True)

current = fs.head

# Walk through the file directory and print each folder or files name
while current:
    print(current.name)
    current = current.next

print([child.name for child in folder1.children])  # [Resume.docx, Photos] photos being another directory 
print(pics.is_directory)                           # True'
'''