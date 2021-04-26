class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtPosition(head,position,data):
    node = SinglyLinkedListNode(data)
    index = 0
    iterator = head

    while iterator is not None:
        if index == position:
            tmp = iterator.next
            iterator.next = node
            node.next = tmp
            return head
        index += 1
        iterator = iterator.next
    return head
