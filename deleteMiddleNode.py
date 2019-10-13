from linkedList import LinkedList


def deleteMiddleNode(linkedList, node):
    current = linkedList.head
    if(current.value == node):
        return linkedList
    while(current.next):
        if(current.next.value == node and current.next.next != None):
            current.next = current.next.next
            break
        elif(current.next.value == node and current.next.next == None):
            return linkedList
        current = current.next
    return linkedList


myLinkedList = LinkedList(1)
myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.append(7)
myLinkedList.append(8)
myLinkedList.append(9)
deleteMiddleNode(myLinkedList, 8).print()
