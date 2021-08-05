# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def getEvenDigits(n,i=0,x=0):
    if(n == 0):
        return x
    else:
        rem = n%10
        if(rem % 2 == 0):
            x += rem*(10**(i))
            i+=1 
        return getEvenDigits(n//10,i,x)
        
def onlyEvenDigitsHelper(l,res=[]):
    if(l == []):
        return res
    else:
        res.append(getEvenDigits(l[0]))
        return onlyEvenDigitsHelper(l[1:],res)
        
def fun_recursion_onlyevendigits(l): 
    if(l == []):
        return []
    return onlyEvenDigitsHelper(l,[])
