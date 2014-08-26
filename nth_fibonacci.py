from math import floor, sqrt
def nth_fibonacci(n):
    n = int(n)
    phi = (1+5**.5)/2
    return int(floor((phi**n)/sqrt(5)+.5))