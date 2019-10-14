from linkedList import LinkedList

# time complexity is O(nlogn + n) = o(nlogn)
# space complexity is o(n) which is an array of size n


def partition(linkedList, value):
    arr = []
    current = linkedList.head
    while(current):
        arr.append(current.value)
        current = current.next
    arr = sorted(arr)
    current = linkedList.head
    for i in range(0, len(arr)):
        if (i == 0):
            linkedList.head.value = arr[i]
        else:
            current.value = arr[i]
        current = current.next
    return linkedList


def partitionTwo(linkedList, value):
    myLinkedList = LinkedList(None)
    current = linkedList.head
    while(current):
        if(current.value < value):
            myLinkedList.prepend(current.value)
        elif(current.value >= value):
            myLinkedList.append(current.value)
        current = current.next
    current = None
    return myLinkedList


myLinkedList = LinkedList(3)
myLinkedList.append(5)
myLinkedList.append(8)
myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.append(2)
myLinkedList.append(1)
myLinkedList.append(99)
partition(myLinkedList, 5).print()
partitionTwo(myLinkedList, 5).print()
