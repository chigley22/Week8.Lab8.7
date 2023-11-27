from Node import Node
from LinkedList import LinkedList

if __name__ == "__main__":
    int_list = LinkedList()
    
    user_input = input()
    
    # Convert the string tokens into integers and append to intList
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        new_node = Node(num)
        int_list.append(new_node)
    
    search_num = int(input())
    found_node = int_list.search(search_num)
    
    if found_node == None:
        print('%d not found in list.' % search_num)
    else:
        print('%d found in list at position %d.' % (search_num, found_node.node_pos))