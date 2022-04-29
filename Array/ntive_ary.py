''' Move all the negative elements to one side of the array  '''

'''
Test Case 1
input = [-12,-13,1,-2,22,42,-6]
output = [-12,-13,-2,-6,1,22,42]

Test Case 2
input = [1,2,-3,5,-6,-7,8,-9]
output = [-3,-6,-7,-9,1,2,5,8]
'''


def ntary(l):
    
    '''
    tmp : temp veriable
    '''
    tmp = 0

    #access array 
    for i in range(len(l)):
            if l[i]<0:

                #skip 1st element
                if i==0:
                    continue

                # swap negatives
                while True:
                    
                    if l[i-1]>0:
                        tmp =l[i-1]
                        l[i-1] = l[i]
                        l[i] = tmp    
                        i = i-1
                    
                    else:
                        # break the loop
                        break

    return l

            

