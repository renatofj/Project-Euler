# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. Solution: 142857

def cmp(a, b):
    return (a > b) - (a < b)
	
def sortdigits(x):
	return "".join(sorted(str(x)))

i = 99999

while True:
	s = sortdigits(i)
	
	if cmp(sortdigits(i*2), s) == 0 and cmp(sortdigits(i*3), s) == 0 and cmp(sortdigits(i*4), s) == 0 and cmp(sortdigits(i*5), s) == 0:
		print(i)
		break
		
	i = i + 9