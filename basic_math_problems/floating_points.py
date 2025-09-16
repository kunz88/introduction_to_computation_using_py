""" 11001100110011001100110011001100110011001100110011001
This is equivalent to the decimal number
0.1000000000000000055511151231257827021181583404541015625
Pretty close to 1/10, but not exactly 1/10. 

So, for example, it is better
to write abs(x-y) < 0.0001 rather than x == y.
"""



x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')
print(' x == 10*0.1 =',x == 10*0.1 , 'x', x ,'10*0.1', 10*0.1)