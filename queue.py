class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, data):
        self.head = QueueNode(data)

    def add(self, data):
        if(self.head == None):
            self.head = QueueNode(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = QueueNode(data)

    def remove(self):
        if(self.head == None):
            return "Queue is empty"
        item = self.head
        self.head = self.head.next
        return item.data

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.head == None
