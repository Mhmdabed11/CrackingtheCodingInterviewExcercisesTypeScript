class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = data


class Stack:
    def __init__(self, data):
        self.top = StackNode(data)

    def push(self, data):
        if(self.top == None):
            self.top = StackNode(data)
            return
        else:
            item = StackNode(data)
            if(data > self.top.min):
                item.min = self.top.min
            item.next = self.top
            self.top = item

    def pop(self):
        if(self.top == None):
            raise Exception('Stack is empty')
        item = self.top
        self.top = self.top.next
        return item.data

    def peek(self):
        if(self.top == None):
            raise Exception('Stack is empty')
        else:
            return self.top.data

    def minimum(self):
        if(self.top == None):
            raise Exception('Stack is Empty')
        else:
            return self.top.min


MyStack = Stack(1)
MyStack.push(2)
MyStack.push(4)
MyStack.push(6)
MyStack.push(-131230)
print(MyStack.minimum())
