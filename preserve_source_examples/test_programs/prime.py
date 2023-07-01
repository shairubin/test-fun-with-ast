# A utility function that returns true if x is a prime


def isPrime(x):
    check = False
    if (x ==1):
        check = True
        return check
    elif x > 1:
        for i in range( 2, x):
            if (x % i == 0):
                check = True
                break
            else:
                check = False
    return check


# checker that was used in fib.py
for i in range(1, 15):
    if isPrime(i) == True:
        print('fun with ast')
        print(i, 'is a Prime Number')
    else:
        print(i, 'is a not Prime Number')












