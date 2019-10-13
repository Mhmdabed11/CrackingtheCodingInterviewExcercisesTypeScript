from linkedList import LinkedList
from hashTable import HashTable

# remove dups with hashTable


def removeDups(linkedList):
    myHashTable = HashTable()
    current = linkedList.head
    while(current):
        myHashTable.put(current.value, "node")
        current = current.next
    entries = myHashTable.getEntries()
    current = linkedList.head
    for i in range(0, len(entries)):
        if (i == 0):
            linkedList.head.value = entries[i]['key']
        else:
            current.next.value = entries[i]['key']
            current = current.next
    current.next = None
    return linkedList

# remove dups with dictionary


def removeDupsTwo(linkedList):
    myDict = {}
    current = linkedList.head
    while(current):
        myDict[current.value] = "node"
        current = current.next
    itr = 0
    myCurrent = None
    for key in myDict.keys():
        if(itr == 0):
            linkedList.head.value = key
            myCurrent = linkedList.head
        else:
            myCurrent.next.value = key
            myCurrent = myCurrent.next
        itr = itr+1
    myCurrent.next = None
    return linkedList


def removeDupsThree(linkedList):
    ptr1 = linkedList.head
    while(ptr1.next):
        ptr2 = ptr1
        while(ptr2.next):
            if(ptr2.next.value == ptr1.value):
                ptr2.next = ptr2.next.next
            else:
                ptr2 = ptr2.next
        ptr1 = ptr1.next
    return linkedList


myLinkedList = LinkedList(1)
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(3)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(1)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(3)
myLinkedList.append(3)
myLinkedList.append(8)
myLinkedList.append(99)
myLinkedList.append(100)
myLinkedList.append(5)
myLinkedList.append(5)
myLinkedList.append(6)
# removeDupsTwo(myLinkedList).print()
# removeDups(myLinkedList).print()
removeDupsThree(myLinkedList).print()
