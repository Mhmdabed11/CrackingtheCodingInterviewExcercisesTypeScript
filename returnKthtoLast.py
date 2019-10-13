from linkedList import LinkedList


def returnKthToLast(linkedList, k):
    ptr1 = linkedList.head
    ptr2 = linkedList.head
    for i in range(0, k-1):
        try:
            ptr2 = ptr2.next
        except Exception as exception:
            return exception
    while(ptr1.next and ptr2.next):
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1.value


myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.append(6)


print(returnKthToLast(myLinkedList, 3))
