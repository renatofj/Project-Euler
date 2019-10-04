import math

def ispentagonal(n):
    s = (math.sqrt(24*n+1)+1)/6
    return s == int(s)

def pentagonal():
    n = 1
    
    while True:
        yield (n*(3*n-1))/2
        n += 1

def solution():
    for pj in pentagonal():
        for pk in pentagonal():
            if pj != pk and ispentagonal(abs(pj-pk)) and ispentagonal(pj+pk):
                print(pj)
                print(pk)
                return abs(pj-pk)
        
print(solution())