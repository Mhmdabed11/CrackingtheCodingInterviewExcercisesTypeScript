def getIndexFromHashcode(hashCode, list=[]):
    arrayLength = len(list)
    indexFromHashcode = (hashCode % arrayLength + arrayLength) % arrayLength
    return indexFromHashcode
