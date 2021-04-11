class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListSearch(head,data):
    index = 0
    while head is not None:
        if head.data is data:
            return index
        index += 1
        head = head.next
    return -1
