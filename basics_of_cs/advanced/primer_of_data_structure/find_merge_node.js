class SinglyLinkedListNode{
    constructor(data) {
        this.data = data;
        this.next = null;
    }
  }

function findMergeNode(headA,headB){
    let = intersection = -1
    let currentNodeA = headA
    let currentNodeB = headB

    while (currentNodeA != null) {
        while (currentNodeB != null) {
            if (currentNodeA.data != currentNodeB.data) {
                currentNodeB = currentNodeB.next
                continue
            }
            intersection = currentNodeA.data
            while (currentNodeB.next != null) {
                if (currentNodeA.next == null ) {
                    intersection = -1
                    break
                }
                currentNodeA = currentNodeA.next
                currentNodeB = currentNodeB.next
                if (currentNodeB.data != currentNodeA.data) {
                    intersection = -1
                    break
                }
            }
            currentNodeB = currentNodeB.next
        }
        currentNodeA = currentNodeA.next
        currentNodeB = headB
    }
    return intersection
}
