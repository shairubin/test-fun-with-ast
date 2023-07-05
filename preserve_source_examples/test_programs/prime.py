# A utility function that returns true if x is a prime


def isPrime(x):
    pass
    if (x < 2):
        return True
    else:
        for i in range(2, x): # if you add a space before 2 fun-with-ast breaks
            pass
            if (x % i == 0):
                return False
    return True


# checker that was used in fib.py
print('fun with ast')
for i in range(1, 15):
    if isPrime(i):
        print(i, 'is a Prime Number')
    else:
        print(i, 'is a not Prime Number')












