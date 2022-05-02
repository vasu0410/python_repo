''' Given two sorted arrays arr1 and arr2. 
    Each array is sorted in non-decreasing order. Merge the two arrays 
    into one sorted array in non-decreasing order without using any extra space.
    
    Test Case 1:
    
    input  : arr1 = [1,3,5,7] ,arr2 = [0,2,6,8,9]
    output : [0,1,2,3,5,6,7,8,9]
    
    Test Case 2:
    input  : arr1 = [10,12] , arr2 = [5,18,20]
    output : [5,10,12,18,20]
'''

def mrg_arr(arr1,arr2):
    '''
    m : length of array 1
    n : length of array 2
    '''

    m,n = len(arr1),len(arr2)
    for i in range(n):
        
        for j in range(m):
            
            # if element of array 2 less then arr1 swap the value 
            if arr2[i]<arr1[j]:
                arr2[i],arr1[j] = arr1[j],arr2[i]
    
    #sort merge array
    arr1.sort()
    arr2.sort()            

    # merge arr2 in arr1
    arr1.extend(arr2)

    return arr1
    
