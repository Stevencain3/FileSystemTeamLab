# Node represents a file or directory
class Node:
    def __init__(self, name, is_directory=True):
        self.name = name
        self.is_directory = is_directory
        self.content = "" if not is_directory else None
        self.children = [] if is_directory else None
        self.prev = None
        self.next = None