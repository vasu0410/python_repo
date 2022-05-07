'''Given an array of intervals where intervals[i] = [starti, endi], merge all 
    overlapping intervals, and return an array of the non-overlapping intervals 
    that cover all the intervals in the input.
    
    Test Case 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    
    Test Case 2:
    
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.'''


def mrg_interval(arr):
    '''
    arr : input array
    arr1 : to store merge intervels 
    tmp : to store array 1st element
    '''
    arr.sort()
    arr1 = []
    tmp = arr[0]

    # if array length is 1 return orignal array as ouput
    if len(arr)==1:
            return arr

    for i in range(1,len(arr)):

        # check if tmp last value is grater than array i'th list last element
        if tmp[-1] >= arr[i][0]:
            
            #store maximum value from i'th element last value and tmp last value
            tmp[-1] = max(arr[i][-1],tmp[-1])

        else:
            # to store arr1
            arr1.append(tmp) 

            # store array i'th value   
            tmp = arr[i]

        # if i value is equals to array length - 1 which is also last value of i then store tmp value to arr1
        if i==len(arr)-1:
            arr1.append(tmp)        
    
    return arr1
