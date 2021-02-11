class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteTail(head):
    # 要素数が1なら削除しない
    if head.next is None:
        return head

    iterator = head
    while iterator.next.next is not None:
        iterator = iterator.next
    iterator.next = None
    return head
