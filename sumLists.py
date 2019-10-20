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


class PartialSum:
    sum = LinkedList()
    carry = 0


def sumTwoListsTwo(node1, node2):
    if(node1 == None and node2 == None):
        sum = PartialSum()
        return sum
    sum = sumTwoListsTwo(node1.next, node2.next)
    val = node1.value + node2.value + sum.carry
    sum.sum.prepend(val % 10)
    sum.carry = math.floor(val / 10)
    return sum


def addLists(linkedList1, linkedList2):
    l1 = linkedList1.length()
    l2 = linkedList2.length()

    if(l1 > l2):
        for i in range(0, l1-l2):
            linkedList2.prepend(0)
    elif(l2 > l1):
        for i in range(0, l2-l1):
            linkedList1.prepend(0)

    sum = sumTwoListsTwo(linkedList1.head, linkedList2.head)
    sum.sum.prepend(sum.carry)
    return sum.sum


myLinkedList1 = LinkedList(9)
myLinkedList1.append(9)
myLinkedList1.append(9)


myLinkedList2 = LinkedList(9)
myLinkedList2.append(9)
myLinkedList2.append(9)
myLinkedList2.append(7)
myLinkedList2.append(6)


addLists(myLinkedList1, myLinkedList2).print()
