class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value == None:
            self.head = None
        else:
            self.head = LinkedListNode(value)

    def append(self, value):
        if self.head == None:
            self.head = LinkedListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = LinkedListNode(value)

    def prepend(self, value):
        if self.head == None:
            self.head = LinkedListNode(value)
        else:
            newHead = LinkedListNode(value)
            newHead.next = self.head
            self.head = newHead

    def print(self):
        arr = []
        current = self.head
        while(current):
            arr.append(current.value)
            current = current.next
        print(arr)


myLinkedList = LinkedList(3)
myLinkedList.append(4)
myLinkedList.prepend(10)
