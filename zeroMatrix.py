from hashTable import HashTable

# time complexity: O(mn)


def zeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    iHashTable = HashTable()
    jHashTable = HashTable()
    for i in range(0, m):
        for j in range(0, n):
            if(matrix[i][j] == 0):
                iHashTable.put(i, "i")
                jHashTable.put(j, "j")
    ientries = iHashTable.getEntries()
    jentries = jHashTable.getEntries()

    for i in range(0, len(ientries)):
        for j in range(0, n):
            matrix[ientries[i]['key']][j] = 0
    for i in range(0, len(jentries)):
        for j in range(0, m):
            matrix[j][jentries[i]['key']] = 0
    return matrix


print(zeroMatrix([[1, 0, 3], [8, 5, 6], [7, 8, 9], [10, 11, 14]]))
