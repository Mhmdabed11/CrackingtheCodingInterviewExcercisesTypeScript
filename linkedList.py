class LinkedListNode :
    def __init__(self,value):
        self.value=value;
        self.next=None;


class LinkedList:
    head = None;
    def __init__(self,value):
        self.head = LinkedListNode(value)
    def append(self,value):
        if self.head == None:
            self.head = LinkedListNode(value)
            return;
        current = self.head;
        while current.next:
            current=current.next;
        current.next = LinkedListNode(value)
    def prepend(self,value):
        if self.head == None:
            self.head = LinkedListNode(value)
        current = self.head;
        newHead = LinkedListNode(value);
        newHead.next = self.head;
        self.head = newHead;

myLinkedList = LinkedList(3)
myLinkedList.append(4)
myLinkedList.prepend(10)