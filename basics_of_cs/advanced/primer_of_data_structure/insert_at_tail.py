class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtTail(head,data):
    iterator = head
    while iterator.next is not None:
        iterator = iterator.next
    iterator.next = SinglyLinkedListNode(data)
    return head
