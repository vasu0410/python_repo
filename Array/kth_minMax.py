''' kth min and max values '''

'''
Test case 1
input = [7,10,4,3,20,15] k=3
output = 10 7

Test case 2
input = [3,2,3,1,2,4,5,5,6] k=4
output = 4 3
'''

def kth_maxMin(l,k):
    '''
    l : list
    n : min value
    n : max value
    '''
    #sorting list
    l.sort()
    
    # for kth min
    n = l[k-1]
    
    # for kth max
    m = l[len(l)-k]

    return f'{m} {n}'
