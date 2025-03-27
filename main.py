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

      # seting up the Drives under this_pc
    c_drive = fs.add_to_directory(this_pc, "C Drive")
    d_drive = fs.add_to_directory(this_pc, "D Drive")

    # Subfolders under each drive
    docs = fs.add_to_directory(c_drive, "Documents")
    one = fs.add_to_directory(d_drive, "OneDrive")

    # Sample files
    fileNode = fs.add_to_directory(docs, "readme.txt", is_directory=False)
    #this would be how you add content(write)  just make a function that we can call to do this aswell as specify what node we want to change
    fileNode.content = ("This is the content inside a read me.txt ")
    # print(fileNode.content) // this would be how we print out (read) the content 
    fs.add_to_directory(one, "studentFile.txt", is_directory=False)
  
    # sends back all of these things down to main for use
    return fs, root, this_pc, c_drive, docs, d_drive, one 

def read_file(file):
    if not file.is_directory:
        print(f"Reading file '{file.name}': {file.content}")
        return file.content
    print(f"'{file.name}' is a directory, not a file.")
    return None

def write_file(file, newContent):
    if not file.is_directory:
        file.content = newContent
        print(f"File '{file.name}' overwitten with new content.")
        return
    print(f"'{file.name}'is a directory, not a file.")
   


# Print full paths from root to files/folders
def print_paths(node, path=""):
    current_path = f"{path}{node.name}"
    if node.is_directory and node.children: #checks if the node is a directory and has children 
        for child in node.children: # goes through each child and recuseifly goes threw all the children and adds it to the curent path and restarts the process
            print_paths(child, current_path + " > ")
    else: # once there is no more children under neith then it prints out the curnt path 
        print(current_path)
        
#testing

# this is basically giving the main all of these variables for we vcan use them in the main / global scope 
fs, root, this_pc, c_drive, docs, d_drive, one = setup_file_structure()

print("Initial File System Structure:")
print_paths(root)

file_name = input("Enter file name to write to: ")
newContent = input("Enter new content: ")
for child in root.children:
        if child.name == file_name:
            fs.write_file(child.name, newContent)
            
      

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