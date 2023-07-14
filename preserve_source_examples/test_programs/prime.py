# A utility function that returns true if x is a prime

def isPrime(x):
    if (x<2):                      # <-- note the changes in unparse here
        return True
    else:
        for i in range( 2 ,  x ):  # <-- note the changes in unparse here
            if (x %i ==0):         # <-- note the changes in unparse here
                return False
    return True


# checker that was used in fib.py
print('fun with ast')
for (i) in range( 1, 15 ):         # <-- note the changes in unparse here
    if isPrime(i):
        print(i, 'is a Prime Number')
    else:
        print(i, 'is a not Prime Number')

