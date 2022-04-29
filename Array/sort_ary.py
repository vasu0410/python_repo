'''Sorting array of only 0,1 and 2. without sort function '''

'''
Test case 1
input = [0,1,0] 
output = 0 0 1

Test case 2
input = [0,2,1,2,0] 
output = 0 0 1 2 2
'''


def sortary(arr):
    '''
    tmp : empty list
    tmp1 : tamp variable
    arr : input list
    '''
    tmp = 0
    tmp1 = []

    #loop
    while len(arr) > 0:
        
        #store 1st element
        tmp = arr[0]

        for i in arr:

            if tmp>=i:
                tmp = i
        
        # remove used element
        arr.pop(arr.index(tmp))
        
        # store sorted element 
        tmp1.append(tmp)
        
    return tmp1
