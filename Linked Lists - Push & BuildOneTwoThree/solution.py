from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):

    new_head = Node(data)
    new_head.next = head

    return new_head

def build_one_two_three():

    cur_node = old_node = head = None

    for value in range(3):

        cur_node = Node(value + 1)

        if old_node is not None:
            old_node.next = cur_node

        else:
            head = cur_node

        old_node = cur_node

    return head
