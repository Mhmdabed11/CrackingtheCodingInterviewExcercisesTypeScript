from linkedList import LinkedList
from hashTable import HashTable


def loopDetection(linkedList):
    myHashTable = HashTable()
    current = linkedList.head
    while(current.next):
        if(myHashTable.get(current)):
            return current
        else:
            myHashTable.put(current, current.value)
        current = current.next


myLinkedList = LinkedList()
myLinkedList.append('A')
myLinkedList.append('B')
myLinkedList.append('C')
myLinkedList.append('D')
p = myLinkedList.head
while(p.next):
    p = p.next
p.next = myLinkedList.head

print(loopDetection(myLinkedList).value)
