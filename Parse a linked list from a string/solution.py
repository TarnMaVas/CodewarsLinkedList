def linked_list_from_string(s):
    if not s or s == 'None':
        return None

    values = s.split(' -> ')
    head = Node(int(values[0]), None)
    node = head

    for entry in values[1:-1]:
        new_node = Node(int(entry), None)
        node.next = node = new_node

    return head
