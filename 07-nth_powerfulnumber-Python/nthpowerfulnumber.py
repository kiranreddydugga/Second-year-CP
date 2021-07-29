# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def numSquareSum(n):
    squareSum = 0;
    while(n>0):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum

# method return true if
# n is Happy number
def ishappynumber(n):
    # initialize slow
    # and fast by n
    slow = n;
    fast = n;
    while(True):

        # move slow number
        # by one iteration
        slow = numSquareSum(slow);
        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;

    # if both number meet at 1,
    # then return true
    if (slow == 1):
        return True
    else:
        return False

def nth_happy_number(n):
    
    found = 1
    guess = 0
    while (found <= abs(n)):
        guess += 1
        if(ishappynumber(guess)):
            found += 1
    return guess