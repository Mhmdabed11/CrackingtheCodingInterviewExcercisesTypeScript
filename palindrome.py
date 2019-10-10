import math


def palindrome(str):
    isPalindrome = True
    if str == None:
        return False
    for i in range(0, math.floor(len(str)/2)):
        if(str[i] != str[len(str)-1-i]):
            isPalindrome = False
            break
    return isPalindrome


print(palindrome("mohammad abed"))
