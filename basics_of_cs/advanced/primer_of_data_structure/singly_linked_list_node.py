class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtHead(head,data):
    node = SinglyLinkedListNode(data)
    node.next = head
    while node is not None:
        print(node.data, end ="➡")
        node = node.next
