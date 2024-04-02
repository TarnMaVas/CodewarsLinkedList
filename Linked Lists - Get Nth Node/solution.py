from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if not isinstance(index, int) or index < 0 or node is None:
        raise ArgumentError

    for _ in range(index):
        if node is None:
            raise ArgumentError

        node = node.next

    if node is None:
        raise ArgumentError

    return node
