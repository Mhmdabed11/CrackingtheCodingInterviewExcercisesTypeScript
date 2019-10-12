
# time complexity is o(n)


def stringCompression(word):
    result = word[0]
    count = 1
    for i in range(0, len(word)-1):
        if(word[i] == word[i+1]):
            count = count+1
        if(word[i] != word[i+1]):
            result = result + str(count) + word[i+1]
            count = 1
    result = result + str(count)
    return result


print(stringCompression('aabbccddefgeerrtt'))
