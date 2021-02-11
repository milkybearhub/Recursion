class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMinNum(head):
    counter = 0
    min_index = 0
    min_data = head.data
    while head is not None:
        if head.data < min_data:
            min_index = counter
            min_data = head.data
        counter += 1
        head = head.next
    return min_index

    # 配列に突っ込んで最後に最小値を判定する
    # counter = 0
    # linked_list = []
    # while head is not None:
    #     linked_list.append(head.data)
    #     head = head.next
    # return linked_list.index(min(linked_list))
