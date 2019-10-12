from linkedList import LinkedList
from getIndexFromHashCode import getIndexFromHashcode
from hashCode import generateHashCode


class HashTable:
    array = [None]*10

    def put(self, key, value):
        keyHashCode = generateHashCode(key)
        index = getIndexFromHashcode(keyHashCode, self.array)
        if self.array[index] == None:
            self.array[index] = LinkedList([key, value])
        elif self.array[index] != None and type(self.array[index] is LinkedList):
            current = self.array[index].head
            found = False
            while(current):
                if current.value[0] == key:
                    current.value[1] = value
                    found = True
                    break
                current = current.next
            if found == False:
                self.array[index].append([key, value])

    def get(self, key):
        keyHashCode = generateHashCode(key)
        index = getIndexFromHashcode(keyHashCode, self.array)
        if(self.array[index] == None):
            return None
        currentLinkedList = self.array[index]
        current = currentLinkedList.head
        while(current):
            if (current.value[0] == key):
                return current.value[1]
            current = current.next

    def getEntries(self):
        entries = []
        for i in range(0, len(self.array)):
            if(self.array[i] != None):
                currentLinkedList = self.array[i]
                current = currentLinkedList.head
                while(current):
                    entries.append(
                        {"key": current.value[0], "value": current.value[1]})
                    current = current.next
        return entries
