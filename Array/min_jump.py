'''Find the minimum number of jumps to reach the end of the array (starting from the first element). 
    If an element is 0, then you cannot move through that element.

    Note: Return -1 if you can't reach the end of the array.
    
    Test Case 1:
        input = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
        output = 3

    Test Case 2:
        input = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
        ouput = 4

        invelid 
        output = 6 
        becuse problem say minumum jump so 6 is not right answer     
        '''


def min_jump(arr):
    '''
    step : show step of each element 
    maxx : show max reach of array element for jump
    jump : no of jump 
    n    : length of array '''

    #arr[0] is first element of array
    step = arr[0]
    maxx = arr[0]

    #initial value of jump is 1 
    jump = 1
    n = len(arr)
    
    # array have only one element then output is 0
    if n==1:
        return 0

    # array first element is zero then return -1 as mention in problem becuase 
    # 0 value not reach to the end of array    
    elif arr[0]==0:
        return -1

    else:
        for i in range(1,n):

            # if i is last element then return jump value
            if i==n-1:
                return jump

            # store max value of index reach
            maxx = max(maxx,i+arr[i])

            # step decrasing on every loop
            step -= 1

            # there is no step left then jump value is increase by one
            if step ==0:
                jump +=1
                
                # if i value is more than max reach of index then ans will be -1
                if i>=maxx:
                    return -1

                #store stap of i'th element
                step = maxx-i             
    
    
        