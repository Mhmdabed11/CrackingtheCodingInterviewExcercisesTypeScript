from linkedList import LinkedList
from hashTable import HashTable


def reverseLinkedList(linkedList):
    current = linkedList.head
    while(current.next):
        linkedList.prepend(current.next.value)
        current.next = current.next.next
    return linkedList


def reversedLinkedList(linkedList):
    resultLinkedList = LinkedList()
    current = linkedList.head
    while(current):
        resultLinkedList.prepend(current.value)
        current = current.next
    return resultLinkedList


def linkedListPalindrome(linkedList):
    myHashTable = HashTable()
    pointer = linkedList.head
    while(pointer):
        if(myHashTable.get(pointer.value)):
            myHashTable.put(pointer.value, myHashTable.get(pointer.value) + 1)
        else:
            myHashTable.put(pointer.value, 1)
        pointer = pointer.next
    isPalindrome = True
    evenCount = 0
    oddCount = 0
    for i in range(0, len(myHashTable.getEntries())):
        if(myHashTable.getEntries()[i]['value'] % 2 == 0):
            evenCount = evenCount + 1
        else:
            oddCount = oddCount+1
    if(oddCount > 1):
        isPalindrome = False
    return isPalindrome


def linkedListPalindromeTwo(linkedList):
    myReversedLinkedList = reversedLinkedList(linkedList)
    p1 = linkedList.head
    p2 = myReversedLinkedList.head
    isPalindrome = True
    while(p1 and p2):
        if(p1.value != p2.value):
            isPalindrome = False
            break
        p1 = p1.next
        p2 = p2.next
    return isPalindrome


myLinkedList = LinkedList()
myLinkedList.append(1)
myLinkedList.append(3)
myLinkedList.append(7)
myLinkedList.append(7)
myLinkedList.append(3)
myLinkedList.append(1)


print(linkedListPalindrome








      (myLinkedList))
print(linkedListPalindromeTwo(myLinkedList))
