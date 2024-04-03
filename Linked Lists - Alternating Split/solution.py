class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ArgumentError('Invalid input list!')
        
    other_head = other_node = head.next
    cur_node = head.next = head.next.next
    
    while cur_node is not None and cur_node.next is not None:
        other_node.next = cur_node.next

        cur_node.next = cur_node.next.next
        other_node = other_node.next
        cur_node = cur_node.next
    
    other_node.next = None

    return Context(head, other_head)
