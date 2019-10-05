# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2^(7830457)+1.
# Find the last ten digits of this prime number. Solution: 8739992577

x = 28433 * pow(2, 7830457, 10**10) + 1
x = x % 10**10

print(x)