from linkedList import LinkedList


def intersection(linkedList1, linkedList2):
    intersectionNode = None
    p1 = linkedList1.head
    p2 = linkedList2.head
    l1 = linkedList1.length()
    l2 = linkedList2.length()

    if(l1 > l2):
        for i in range(0, int(l1-l2)):
            p1 = p1.next
    else:
        for i in range(0, int(l2-l1)):
            p2 = p2.next
    while(p1 and p2):
        if(p1 == p2):
            intersectionNode = p1
            break
        p1 = p1.next
        p2 = p2.next
    return intersectionNode


myLinkedList3 = LinkedList()
myLinkedList3.append(111)
myLinkedList3.append(101)
myLinkedList3.append(102)

myLinkedList1 = LinkedList()
myLinkedList1.append(88)
myLinkedList1.append(2)
myLinkedList1.append(100)

p1 = myLinkedList1.head
while(p1.next):
    p1 = p1.next
p1.next = myLinkedList3.head

myLinkedList2 = LinkedList()
myLinkedList2.append(4)
myLinkedList2.append(9)
myLinkedList2.append(88)
myLinkedList2.append(2)
myLinkedList2.append(100)

p2 = myLinkedList2.head
while(p2.next):
    p2 = p2.next
p2.next = myLinkedList3.head

print(intersection(myLinkedList1, myLinkedList2).value)
