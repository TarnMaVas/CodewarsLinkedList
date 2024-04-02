class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ArgumentError

    source, new_head = source.next, source
    new_head.next = dest
    
    
    return Context(source, new_head)
