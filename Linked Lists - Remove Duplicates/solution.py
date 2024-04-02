class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):

    cur_node = head
    prev_node = None
    
    while cur_node is not None:

        if prev_node is None or prev_node.data != cur_node.data:

            prev_node, cur_node = cur_node, cur_node.next
        
        else:
            
            prev_node.next = cur_node = cur_node.next
    
    return head
