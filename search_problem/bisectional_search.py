"""  We can exploit the fact that numbers are totally
ordered. That is, for any pair of distinct numbers, n1 and n2, either n1 < n2 or
n1 > n2. So, we can think of the square root of x as lying somewhere on the line
0_________________________________________________________max
and start searching that interval. Since we don’t necessarily know where to start
searching, let’s start in the middle.
0__________________________guess__________________________max
If that is not the right answer (and it won’t be most of the time), ask whether
it is too big or too small. If it is too big, we know that the answer must lie to the
left. If it is too small, we know that the answer must lie to the right. We then repeat the process on the smaller interval. Figure 3.4 contains an implementation
and test of this algorithm. """


x = 123456789
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
print('exit value',abs(ans**2 - x))

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
numGuessesNR = 0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuessesNR += 1
print('Square root of', k, 'is about', guess)

if(numGuesses > numGuessesNR):
    print('1°- Newton-Raphson search took', numGuessesNR, 'guesses')
    print('2°- Bisection search took', numGuesses, 'guesses')
else:
    print('1°- Bisection search took', numGuesses, 'guesses')
    print('2°- Newton-Raphson search took', numGuessesNR, 'guesses')