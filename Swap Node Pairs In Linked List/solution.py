from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    head.next, prev, head, head.next = head.next.next, head, head.next, head
    
    cur_node = head.next.next

    while cur_node is not None and cur_node.next is not None:
        prev.next = cur_node.next
        cur_node.next, cur_node, cur_node.next = cur_node.next.next, cur_node.next, cur_node
        prev = cur_node.next
        cur_node = cur_node.next.next
    
    return head
