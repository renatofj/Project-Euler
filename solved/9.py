# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 1000):
	for b in range(a, 1000):
		c = 1000 - b - a
		
		if a*a + b*b == c*c:
			print(a)
			print(b)
			print(c)
			print(a*b*c)
			break


