''' Find the maximum and minimum element in an array '''

'''
Test case 1
input = [1,2,3,4,5,6,7,8,9]
ouput = 9 1

Test case 2
input = [100,52,77,80,32,9,24]
ouput = 100 9

'''
def maxmin(l):
    '''
    l : list
    m : max value
    n : min value
    '''
    # input 1st element 
    m = l[0]     
    n = l[0]    

    #for loop to find max and min value
    for i in l:
        if m<=i:
            m = i

        if n>=i:
            n = i 

    return f"{m} {n}"

