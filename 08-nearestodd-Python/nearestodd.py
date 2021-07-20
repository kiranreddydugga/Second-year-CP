# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
    if type(n) == int:  
        if n % 2 == 0:
            return n - 1
        else:
            return n
    else:  
        temp = int(n) 
        up_sub = abs(temp + 1 - n)
        down_sub = abs(temp - 1 - n)
        if temp % 2 != 0:  
            return temp
        else:  
            if up_sub < down_sub:
                return temp + 1
            else:
                return temp - 1


