""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        return Node(data)

    cur_node = head
    
    if data < cur_node.data:

        new_node = Node(data)
        new_node.next = head
        return new_node

    while cur_node.next is not None:

        if cur_node.data < data < cur_node.next.data:
            new_node = Node(data)
            new_node.next = cur_node.next
            cur_node.next = new_node
            return head
        
        cur_node = cur_node.next
    
    cur_node.next = Node(data)
    return head
