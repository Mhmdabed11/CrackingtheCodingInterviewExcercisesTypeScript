class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, data):
        self.top = StackNode(data)

    def pop(self):
        if(self.top == None):
            return "Stack is empty"
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, value):
        if(self.top == None):
            self.top = StackNode(value)
            return
        item = StackNode(value)
        item.next = self.top
        self.top = item

    def peek(self):
        if(self.top == None):
            return None
        return self.top.data

    def isEmpty(self):
        return self.top == None
