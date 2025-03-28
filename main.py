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
        
        
        
def remove_node(fs, node):
        # Handle file removal
        print(f"Deleting file: {node.name}")
        # Remove from the parent's children list
        parent = find_parent(fs.head, node)
        if parent:
            parent.children.remove(node)
        
        # Remove from linked list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == fs.head:  # If it's the head of the linked list
            fs.head = node.next
        if node == fs.tail:  # If it's the tail of the linked list
            fs.tail = node.prev

        print(f"Successfully deleted: {node.name}")




def find_parent(root, child_node):
    #Helper function to find the parent of a given node
    for child in root.children:
        if child == child_node:
            return root
        if child.is_directory:
            parent = find_parent(child, child_node)
            if parent:
                return parent
    return None
        
#testing
'''
# this is basically giving the main all of these variables for we vcan use them in the main / global scope 
fs, root, this_pc, c_drive, docs, d_drive, one = setup_file_structure()

print("Initial File System Structure:")
print_paths(root)

file_name = input("Enter file name to write to: ")
newContent = input("Enter new content: ")
for child in root.children:
        if child.name == file_name:
            fs.write_file(child.name, newContent)
            
      
'''
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
def main():
    # Initialize the file system structure
    fs, root, this_pc, c_drive, docs, d_drive, one = setup_file_structure()

    while True:
        print("\n--- File System ---")
        print("1. View file system structure")
        print("2. Read a file")
        print("3. Write to a file")
        print("4. Create a new file/folder")
        print("5. Delete a file/folder")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            print("\nFile System Structure:")
            print_paths(root)

        elif choice == '2':
            # Ask for a file name to read
            file_name = input("Enter file name to read: ")
            file = find_file(root, file_name)

            if file:
                read_file(file)
            else:
                print(f"File '{file_name}' not found.")

        elif choice == '3':
            # Ask for a file name and new content to write
            file_name = input("Enter file name to write to: ")
            new_content = input("Enter new content: ")

            file = find_file(root, file_name)

            if file:
                write_file(file, new_content)
            else:
                print(f"File '{file_name}' not found.")

        elif choice == '4':
            # Ask to create a new file or folder
            parent_name = input("Enter parent directory name: ")
            parent = find_file(root, parent_name)

            if parent and parent.is_directory:
                new_name = input("Enter the name of the new file/folder: ")
                is_directory = input("Is this a directory? (y/n): ").lower() == 'y'
                new_node = fs.add_to_directory(parent, new_name, is_directory)

                print(f"New {'directory' if is_directory else 'file'} '{new_name}' created.")
            else:
                print(f"'{parent_name}' is not a valid directory.")

        elif choice == '5':
            # Ask for a file/folder to delete
            file_name = input("Enter file name to delete: ")
            file = find_file(root, file_name)

            if file:
                remove_node(fs, file)
                print(f"File '{file_name}' deleted.")
            else:
                print(f"File '{file_name}' not found.")

        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def find_file(node, file_name):
    #Recursive function to find a file or directory by name
    if node.name == file_name:
        return node
    if node.is_directory:
        for child in node.children:
            result = find_file(child, file_name)
            if result:
                return result
    return None



if __name__ == "__main__":
    main()