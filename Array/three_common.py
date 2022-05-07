''' Given three arrays sorted in increasing order. Find the elements that are common 
    in all three arrays.

    Test Case 1:

    Input: A = [1, 5, 10, 20, 40, 80],B = [6, 7, 20, 80, 100],
           C = [3, 4, 15, 20, 30, 70, 80, 120]

    Output: 20 80
    
    Input : A = [1, 1, 2, 5, 9],B = [1,2,3,4,5,5],
            C = [1,3,5,7,9]
    Explanation: 20 and 80 are the only
    common elements in A, B and C.'''

def comman_element(arr1,arr2,arr3):
    '''com_ele : to store common element
       arr1,arr2,arr3 : to store input arry1,arry2,arr3 value
       '''

    com_ele = 0

    # convert array value to set value    
    arr1 = set(arr1)
    arr2 = set(arr2)
    arr3 = set(arr3)

    # check common element form arr1,arr2 and arr3 and store to com_ele
    com_ele = arr1.intersection(arr2)
    com_ele = com_ele.intersection(arr3)

    # if there is no common element return -1
    if com_ele == 0:
        return -1

    com_ele = list(com_ele)
    com_ele.sort()
    # return in list type 
    return com_ele       
