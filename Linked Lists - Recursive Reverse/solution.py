class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, tail = None):
    
    if head is None:
        return tail

    new_tail = Node(head.data)
    new_tail.next = tail

    return reverse(head.next, new_tail)
