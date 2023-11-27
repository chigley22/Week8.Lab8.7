class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.node_pos = -1
        
    def print_node_data(self):
        print(self.data, end='')