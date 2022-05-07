''' Write a program to rotate an array by one from left to right  
    example : [1,2,3] change to [3,1,2]

    Test Case 1
        input = [9,8,7,6,4,2,1,3]
        output = [3,9,8,7,6,4,2,1]

    invelid
        ouput = [9,9,8,7,6,4,2,1]

    Test Case 2
        input = {1}
        output = {1}
'''

def rotaAry(arr):
    '''
    tmp : use to store last element of array
    arr : input array 
    '''
    tmp = arr[len(arr)-1]
    
    #loop in reverser order 
    for i in range(len(arr)-1,0,-1):
        
        # store i-1 index value to i index value
        arr[i] = arr[i-1]    
        
        # replace 0 element with last element to complete rotation
        if i==1:
            arr[0]=tmp
          
            
    return arr            
