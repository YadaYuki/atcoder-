def gcd(a,b):
    '''
    Calculate gretest common divisor by euclid mutual division method
    '''
    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(3,6))
print(gcd(-3,6))
print(gcd(-6,6))
print(gcd(-6,-3))

