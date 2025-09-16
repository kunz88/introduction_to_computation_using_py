x,y,z = 10,10,10

if(x % 2 != 0 and y % 2 != 0 and z % 2 != 0):
    print('no one is odd')

if(x >= y and x >= z):
    if(x % 2 == 0):
        print(x)
elif(y >= x and y >= z):
    if(y % 2 == 0):
        print(y)
else:
    if(z% 2 == 0):
        print(z)