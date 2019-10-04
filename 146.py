# The smallest positive integer n for which the numbers n^(2)+1, n^(2)+3, n^(2)+7, n^(2)+9, n^(2)+13, and n^(2)+27
# are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.
# What is the sum of all such integers n below 150 million?

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

x = 10
s = 0

# 150000000

for x in range(10, 1000000, 10):
	x2 = x**2

	if isprime(x2+1) and isprime(x2+3) and not isprime(x2+5) and isprime(x2+7) and isprime(x2+9) and not isprime(x2+11) and isprime(x2+13) and not isprime(x2+15) and not isprime(x2+17) and not isprime(x2+19) and not isprime(x2+21) and not isprime(x2+23) and not isprime(x2+25) and isprime(x2+27) :
		print(x)
		s = s + x
	
print(s)