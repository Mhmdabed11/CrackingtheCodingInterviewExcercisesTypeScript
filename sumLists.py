from linkedList import LinkedList
import math


def sumLists(linkedList1, linkedList2):
    number1 = ""
    number2 = ""
    current1 = linkedList1.head
    while(current1):
        print(current1)
        number1 = number1+str(current1.value)
        current1 = current1.next
    current2 = linkedList2.head
    while(current2):
        number2 = number2 + str(current2.value)
        current2 = current2.next
    number1 = number1[::-1]
    number2 = number2[::-1]
    return int(number1) + int(number2)


def sumListsTwo(linkedList1, linkedList2):
    myLinkedList3 = LinkedList(None)
    carriage = 0
    current1 = linkedList1.head
    current2 = linkedList2.head

    while(current1 or current2):
        if(current1 and current2):
            sum = current1.value + current2.value + carriage
            sumWithoutCarriage = sum
            if(sum >= 10 and current1.next != None and current2.next != None):
                carriage = math.floor(sum/10)
                sumWithoutCarriage = sum % 10
            elif(sum < 10 and current1.next != None and current2.next != None):
                carriage = 0
            myLinkedList3.append(sumWithoutCarriage)
            current1 = current1.next
            current2 = current2.next
        elif(current1 == None):
            myLinkedList3.append(current2.value)
            current2 = current2.next
        elif(current2 == None):
            myLinkedList3.append(current1.value)
            current1 = current1.next
    myLinkedList3.print()


myLinkedList1 = LinkedList(3)
myLinkedList1.append(6)
myLinkedList1.append(5)


myLinkedList2 = LinkedList(2)
myLinkedList2.append(4)
myLinkedList2.append(8)


print(sumListsTwo(myLinkedList1, myLinkedList2))
