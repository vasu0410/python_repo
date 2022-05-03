''' Find the contiguous sub-array(containing at least one number) 
    which has the maximum sum and return its sum.

    Test Case 1:
        input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6

    Test case 2:
        input = [-1,-2,-5,-6]
        
        output = -1

        Invelid output
        output = 0      -0 is not maximum sum in above array

'''


def kadan_algo(arr):
    '''
    maxx : it store max value of input array
    arr : input array
    sum : sum of element store in it
    '''
    maxx = arr[0]
    sum = 0

    for i in arr:
        
        #store sum of array    
        sum += i
       
        
        # store i element to sum if sum is less then i 
        if sum < i:
            sum = i

        # store sum value to maxx if maxx is less then sum 
        if maxx < sum:
            maxx = sum
            
    
    

    return maxx    

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadan_algo(arr))
