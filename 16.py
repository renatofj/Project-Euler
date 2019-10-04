# What is the sum of the digits of the number 2^(1000)? Solution: 1366

f = 2**1000

print f
print sum(map(int, str(f)))