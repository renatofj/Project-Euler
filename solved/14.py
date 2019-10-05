# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def memoize(func):
	cache = dict()
	
	def memoized_func(*args):
		if args in cache:
			return cache[args]
			
		result = func(*args)
		cache[args] = result

		return result

	return memoized_func

def collatzSequenceGenerator(n):
	yield n
	
	if (n > 1):
		if (n % 2 == 0):
			n = n / 2
		else:
			n = 3*n + 1		

		yield from collatzSequence(n)
	
def collatzSequence(n):	
	seq = []
	
	seq.append(n)
	
	if (n > 1):
		if (n % 2 == 0):
			n = n / 2
		else:
			n = 3*n + 1		

		seq.extend(collatzSequence(n))
		
	return seq
	
s, x = 0, 0

memoized_collatzSequence = memoize(collatzSequence)

for i in range(1, 1000000):
	l = len(memoized_collatzSequence(i))
	
	if (l > x):
		s, x = i, l
	
print(s, x)