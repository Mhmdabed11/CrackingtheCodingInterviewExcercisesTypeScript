from hashTable import HashTable

# check if the string is one Way from another string


def oneAway(word1, word2):
    if(word1 == word2):
        return True
    elif (abs(len(word1)-len(word2)) > 1):
        return False
    else:
        edits = 0
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        while(i < m and j < n):
            if(word1[i] != word2[j] and m > n):
                if (edits > 1):
                    break
                edits = edits + 1
                i = i+1
            elif(word1[i] != word2[j] and n > m):
                if (edits > 1):
                    break
                edits = edits+1
                j = j+1
            elif(word1[i] != word2[j] and n == m):
                edits = edits+1
                i = i+1
                j = j+1
            else:
                i = i+1
                j = j+1
    return edits <= 1


print(oneAway('peaks', 'geeks'))
