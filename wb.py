""" 
Given an list nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Example Input: [0,0,11,2,3,4]
Example Output: [11,2,3,4,0,0]
"""
# input list number
# output list number

#look at every number
#decide if number is zero or not
#if zero remove 
#add zero to the end
#if not zero look at the next number


#loop
#conditional compare to zero
#if zero pop
#append zero


def move_zeros(alist):
    output = []
for i in range(len(alist)):
    print(i,alist[1])
    if num == 0:
        alist.pop(i)
        print(alist)
        alist.append(0)
    return alist


print(move_zeros([0,1,0,3,12]))

