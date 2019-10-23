class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, data=None):
        if(data == None):
            self.top = None
            self.length = 0
            return
        self.top = StackNode(data)
        self.length = 1

    def push(self, data):
        if(self.top == None):
            self.top = StackNode(data)
            self.length = self.length+1
            return
        else:
            item = StackNode(data)
            item.next = self.top
            self.top = item
            self.length = self.length+1

    def pop(self):
        if(self.top == None):
            raise Exception('Stack is empty')
        else:
            item = self.top
            self.top = self.top.next
            self.length = self.length-1
            return item.data

    def peek(self):
        if(self.top == None):
            raise Exception('Stack is empty')
        else:
            return self.top.data

    def isEmpty(self):
        return self.top == None

    def getLength(self):
        return self.length


class SetOfStacks:
    def __init__(self, stackSize):
        StackOne = Stack()
        self.stackArray = [StackOne]
        self.stackSize = stackSize

    def push(self, data):
        length = len(self.stackArray)
        index = length - 1
        if(self.stackArray[index].getLength() == self.stackSize):
            newStack = Stack()
            self.stackArray.append(newStack)
            self.stackArray[index+1].push(data)
        else:
            self.stackArray[index].push(data)

    def pop(self):
        length = len(self.stackArray)
        index = length-1
        self.stackArray[index].pop()
        if(self.stackArray[index].getLength() == 0):
            del self.stackArray[index]

    def popAt(self, index):
        if(self.stackArray[index]):
            self.stackArray[index].pop()
        if(self.stackArray[index].getLength() == 0):
            del self.stackArray[index]


MySetOfStacks = SetOfStacks(5)
MySetOfStacks.push(1)
MySetOfStacks.push(2)
MySetOfStacks.push(3)
MySetOfStacks.push(4)
MySetOfStacks.push(5)
MySetOfStacks.push(6)
MySetOfStacks.push(7)
MySetOfStacks.push(8)
MySetOfStacks.push(9)
MySetOfStacks.popAt(0)
MySetOfStacks.popAt(0)
MySetOfStacks.popAt(0)
MySetOfStacks.popAt(0)
MySetOfStacks.popAt(0)
MySetOfStacks.popAt(0)
MySetOfStacks.popAt(0)
print(MySetOfStacks.stackArray[0].top.data)
