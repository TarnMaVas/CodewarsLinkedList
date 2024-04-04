def loop_size(node):

    slow = node
    fast = node
    
    while True:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            result = 0
            
            while True:
                fast = fast.next
                result += 1
                
                if fast == slow:
                    return result
