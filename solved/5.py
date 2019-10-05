# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? Solution: 

def isdivisiblerange(n, x):
	for i in range(1, x + 1):
		if not n % i == 0:
			return False			
	return True

i = 1

while True:
	if isdivisiblerange(i, 20):
		print(i)
		break

	i = i + 1