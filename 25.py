# What is the first term in the Fibonacci sequence to contain 1000 digits? Solution: 4782

import math

def digits(x):
	''' Return amount of digits of x. '''
	return int(math.floor(math.log10(x)) + 1)
	
def fibonacci():
	'''a generator for Fibonacci numbers, goes to next number in series on each call'''
	a, b = 1, 1
	while True:
		yield a
		a, b = b, a + b

f = fibonacci()

i = 1

while True:
	n = f.next()
	
	if digits(n) == 1000:
		print i
		break

	i = i + 1