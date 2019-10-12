from hashTable import HashTable

# palindrome permutaiton using hashTable


def palindromePermutation(string):
    word = string.lower()
    myHashTable = HashTable()
    for i in range(0, len(word)):
        if(myHashTable.get(word[i]) != None):
            myHashTable.put(word[i], myHashTable.get(word[i]) + 1)
        elif (myHashTable.get(word[i]) == None and word[i] != " "):
            myHashTable.put(word[i], 1)

    numOfEvenOccurences = 0
    numOfOddOccurences = 0

    entries = myHashTable.getEntries()
    for i in range(0, len(entries)):
        if(entries[i]['value'] % 2 == 0):
            numOfEvenOccurences = numOfEvenOccurences + 1
        elif (entries[i]['value'] % 2 == 1):
            numOfOddOccurences = numOfOddOccurences + 1

    if(numOfOddOccurences > 1):
        return False
    else:
        return True


# palindrom permutation using dictionary

def palindromePermutationTwo(string):
    word = string.lower()
    charDict = {}
    for i in range(0, len(word)):
        if word[i] in charDict:

            charDict[word[i]] = charDict[word[i]] + 1
        elif word[i] != " ":
            charDict[word[i]] = 1
    numOfEvenOccurences = 0
    numOfOddOccurences = 0
    for value in charDict.values():
        if (value % 2 == 0):
            numOfEvenOccurences = numOfEvenOccurences + 1
        elif (value % 2 == 1):
            numOfOddOccurences = numOfOddOccurences + 1
    return (numOfOddOccurences <= 1)


word = "Never Odd or evensadasdadasd"
print(palindromePermutation(word))
print(palindromePermutationTwo(word))
