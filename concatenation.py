numXs = int(input('How many times want to print x: '))
toPrint = ''

while(numXs > 0):
    toPrint += 'x'
    numXs -= 1
print(toPrint)

num = 0 
count= 0
hasEnterOddNum = False
while(count < 10):
    temp = int(input('Enter a num: '))
    if(temp % 2 == 0):
        hasEnterOddNum = True
    if(temp > num  ):
        num = temp

    count +=1

if(hasEnterOddNum):
    print(num)
else:
    print('The user has not entered odd number')



