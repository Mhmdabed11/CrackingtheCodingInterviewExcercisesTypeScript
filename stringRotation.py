
# time complexit is o(n*substring)


def stringRotation(word1, word2):
    isStringRotation = True
    for i in range(0, len(word2)):
        if(word2[0:i+1] in word1):
            continue
        elif(not word2[i:] in word1):
            isStringRotation = False
    return isStringRotation

# time complexity is o(isSubstring)


def stringRotationTwo(word1, word2):
    result = word1+word1
    return word2 in result


print(stringRotation("watterbottle", "erbottlewat"))
print(stringRotationTwo("watterbottle", "erbottlewat"))
