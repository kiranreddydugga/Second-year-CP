# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
    	# your code goes here
    box = 12
    if(eggs == 0):
        return 0
    elif(1<=eggs<=box):
        return 1
    elif(12<=eggs<=box*2):
         return 2
    elif(24<=eggs<=box*3):
        return 3
    elif(36<=eggs<=box*4):
        return 5
    elif(48<=eggs<=box*5):
         return 5
