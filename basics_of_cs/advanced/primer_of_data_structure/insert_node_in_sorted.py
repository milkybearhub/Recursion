class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeInSorted(head,data):
    node = SinglyLinkedListNode(data)
    currentNode = head

    # 先頭に挿入する場合
    if currentNode.data > node.data:
        node.next = head
        return node
    else:
        while  currentNode.next is not None:
            if currentNode.next.data > node.data:
                node.next = currentNode.next
                currentNode.next = node
                return head
            currentNode = currentNode.next
        currentNode.next = node
        return head
