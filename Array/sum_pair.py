''' Given an array of N integers, and an integer K, find the number of pairs of elements in the array 
    whose k is equal to K.


    Test Case 1:

    Input: K = 6, arr[] = {1, 5, 7, 1}
    Output: 2

    Explanation: 
    arr[0] + arr[1] = 1 + 5 = 6 
    and arr[1] + arr[3] = 5 + 1 = 6.

    Test Case 2:

    Input: K = 2, arr[] = {1, 1, 1, 1}
    Output: 6

    Explanation: 
    Each 1 will produce k 2 with any 1.
    '''

def sum_pair(arr,k):
    '''
    arr  : store input array
    k    : store given sum
    mapp : dictonary to store element and occurrence value
    n    : length of array
    count_pair : store count of pair
    '''

    n = len(arr)
    mapp = {}
    count_pair = 0

    for i in range(n):

        # check k-arr[i] in mapp than count occurance and store in count_pair
        if k - arr[i] in mapp:
            count_pair += mapp[k - arr[i]]
        
        # check if i'th elemnt of array in mapp and increment occurance of i'th element in mapp 
        if arr[i] in mapp:
            mapp[arr[i]] += 1
        
        # if i'th element not in mapp then app mapp i th element with occurance one
        else:
            mapp[arr[i]] = 1
        
        
    return count_pair