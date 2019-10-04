# Find the largest palindrome made from the product of two 3-digit numbers. Solution: 906609 (913 * 993)

def ispalindrome(x):
    string = str(x)
    if string == string[::-1]:
        return True
    else:
        return False
		
max = 0
mx = 0
my = 0
		
for x in range(100, 1000):
	for y in range(100, 1000):
		c = x*y
		if ispalindrome(c):
			if c > max:
				mx = x
				my = y
				max = c
				
print(mx)
print(my)
print(max)