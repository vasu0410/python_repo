''' Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) 
    with 0 sum.
 
    Test Cast 1:

        Input  : [4, 2, -3, 1, 6]
        Output : Yes

        Explanation: 2, -3, 1 is the subarray with sum 0.

    Test Cast 2:

        Input  : [4, 2, 0, 1, 6]
        Output : Yes

        Explanation: 0 is one of the element in the array so there exist a subarray with sum 0.
'''


def subarray_zero(arr):
    '''
    arr  :  input array 
    sum_array : store sum of array element
    n : store givien sum value which is zero
    i : use to as pointer of element
    j : use to as pointer of element
    '''
    sum_array = 0
    n = 0
    i,j = 0,0  

    # if n value already in arr element then return yes , 
    # single elment is also call sub array
    if n in arr:
        return 'Yes'
    
    else:

        while True:

            # j value equal len(arr)-1  
            if j == len(arr)-1:
                return -1
            
            # store sum of arr element
            sum_array += arr[i]

            # if sum_array = n then return yes
            if sum_array == n:
                return 'Yes'

            # if i value become len(arr)-1 rest i position with j+1 and reset sum_array
            if i==len(arr)-1:
 
                i=j+1

                sum_array = 0
                j+=1
                continue
            i += 1    
            
               
                

arr = [1, 4, -2, -2, 5, -4, 3]
print(subarray_zero(arr))