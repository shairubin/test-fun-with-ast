# A utility function that returns true if x is perfect square
import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x                         # <-- note the changes in unparse here


# Returns true if n is a Fibonacci Number, else false

def isFibonacci(n):
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    pass
    A = isPerfectSquare(5 * n * n +4 )         # <-- note the changes in unparse here
    B = isPerfectSquare(5 * n*n - 4)             # <-- note the changes in unparse here
    return A or B
#
#
# # A utility function to test above functions
for i in range( 1, 15):                        # <-- note the changes in unparse here
    if isFibonacci(i) == True:
         print(i, 'is a Fibonacci Number')
    else:
         print(i, 'is a not Fibonacci Number')

