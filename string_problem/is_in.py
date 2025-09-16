def isIn(firstStr,secondStr):
    return firstStr in secondStr or secondStr in firstStr


print(isIn('abc','abcdefgh'))
print(isIn('abcdefgh','cane'))

