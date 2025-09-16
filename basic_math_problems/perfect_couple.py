""" Write a program that asks the user to enter an integer and prints
two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is 
equal to the integer entered by the user.
If no such pair of integers exists, it should print a message to that effect """

x = int(input('Enter an integer: '))
pwr = 2
hasFound = False
while pwr <= 6:
    root = 0
    while root**pwr < abs(x):
        root = root + 1
    if root**pwr == abs(x):
        print(root, 'to the power of', pwr, 'equals', x)
        hasFound = True
        break
    pwr = pwr + 1
if not hasFound:
    print('No such pair of integers exists')