class ThreeInOne:
    def __init__(self, stackSize):
        self.__stackCapaity = stackSize
        self.__array = [None]*3*stackSize
        self.__sizes = [0]*3

    def push(self, stackNum, value):
        if(int(stackNum) > 2):
            print("Stack number should be less than 3")
            return
        if(self.__sizes[stackNum] >= self.__stackCapaity):
            print("%s is full" % stackNum)
            return
        index = stackNum*self.__stackCapaity + self.__sizes[stackNum]
        self.__sizes[stackNum] = self.__sizes[stackNum] + 1
        self.__array[index] = value

    def pop(self, stackNum):
        if(self.__sizes[stackNum] > 0):
            index = self.__stackCapaity * stackNum + (self.__sizes[stackNum]-1)
        else:
            index = self.__stackCapaity * stackNum + self.__sizes[stackNum]
        item = self.__array[index]
        self.__array[index] = None
        if(self.__sizes[stackNum] > 0):
            self.__sizes[stackNum] = self.__sizes[stackNum]-1
        return item

    def peek(self, stackNum):
        if(self.__sizes[stackNum] > 0):
            index = self.__stackCapaity*stackNum + self.__sizes[stackNum]-1
        else:
            index = self.__stackCapaity*stackNum + self.__sizes[stackNum]
        return self.__array[index]

    def isEmpty(self, stackNum):
        return self.__sizes[stackNum] == 0

    def print(self):
        print(self.__array)


MyArrayStack = ThreeInOne(5)
MyArrayStack.push(0, 'a')
MyArrayStack.push(0, 'b')
MyArrayStack.push(0, 'c')
MyArrayStack.push(0, 'd')
MyArrayStack.push(0, 'e')
MyArrayStack.push(1, 'a')
MyArrayStack.push(1, 'b213123123')
MyArrayStack.push(2, 'a')
MyArrayStack.push(2, '898989')
MyArrayStack.push(2, '10293946')
MyArrayStack.pop(1)
MyArrayStack.print()
