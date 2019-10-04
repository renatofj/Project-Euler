# Find the sum of the digits in the number 100! Solution: 648

def factorial(x):
	f = 1
	
	for i in range(1, x + 1):
		f = f * i
	
	return f

f = factorial(100)

print f
print sum(map(int, str(f)))