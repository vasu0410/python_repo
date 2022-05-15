'''Given an array Arr[] that contains N integers (may be positive, negative or zero). 
    Find the product of the maximum product subarray.

    Test Case 1:

        Input: Arr[] = {6, -3, -10, 0, 2}
        Output: 180
        
        Explanation: Subarray with maximum product is [6, -3, -10] which gives product as 180.
    Test Case 2:

        Input: Arr[] = {2, 3, 4, 5, -1, 0}
        Output: 120

    Explanation: Subarray with maximum productis [2, 3, 4, 5] which gives product as 120'''


def sub_product(arr):
    '''
    max_product : store maximum value from prodcut value and element value
    min_product : store minimum value from prodcut value and element value
    ans : store value of maximum sub array of given array
    arr : input array

    '''
    max_product = arr[0]
    min_product = arr[0]
    ans = max_product

    for i in range(1,len(arr)):

        # if element of array is less than 0 than swape the value of max_product and min_product
        if arr[i]<0:

            max_product,min_product = min_product,max_product
        
        # check the value of max and min from element value and element porduct and store in max_product and
        # min_product
        max_product = max(arr[i],max_product*arr[i])
        min_product = min(arr[i],min_product*arr[i])
    
        # store maximum sub array
        ans = max(ans,max_product)

    return ans  


        
