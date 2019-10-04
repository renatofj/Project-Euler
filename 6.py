# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. Solution: 25164150

sumOfSquare = 0
squareOfSum = 0

for x in range(1, 101):
	sumOfSquare = sumOfSquare + x**2
	squareOfSum = squareOfSum + x

diff = squareOfSum**2 - sumOfSquare

print(diff)