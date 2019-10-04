# Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000). Solution: 9110846700

i = 0

for x in range(1, 1001):
	i = i + pow(x, x, 10**10)

print i % 10**10