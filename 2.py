# Find the sum of all the even-valued terms in the sequence which do not exceed four million. Solution: 4613732

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

i = 1
s = 0

while True:
	f = fib(i)
	
	if f <= 4000000:
		if f % 2 == 0:
			s = s + f
	else:
		break
		
	i = i + 1

print (s)