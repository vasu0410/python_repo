''' Given an array of positive and negative numbers, arrange them in an alternate fashion such that every 
    positive number is followed by negative and vice-versa maintaining the order of appearance. 
    Number of positive and negative numbers need not be equal. If there are more positive numbers they appear 
    at the end of the array. If there are more negative numbers, they too appear in the end of the array.

    Test Case 1 : 

    Input  :  arr[] = {1, 2, 3, -4, -1, 4}
    Output : arr[] = {-4, 1, -1, 2, 3, 4}

    Test Case 2 :

    Input  :  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
    output : arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

'''

def rearrange_pos_neg(arr):
    '''
    n : length of array
    tmp : to store temp value 
    '''
    n = len(arr)
    tmp = 0
    
    for i in range(n):
        
        # it check position in 0,2,4,... order or not
        if i%2==0:

            # if value of i'th element is greater than zero or not    
            if arr[i]>0:
            
                for j in range(i,n):
            
                    #check for negative number
                    if arr[j]<0:
                        
                        #store closest negative number in tmp variable
                        tmp = arr[j]
            
                        # this loop use to left rotate array element from i'th to j'th value in reveser order  
                        for k in range(j,i,-1):
                            
                            #store k-1 value to k'th element
                            arr[k] = arr[k-1]
                            
                            # to store i'th elemnt value as tmp
                            if k==i+1:
                                print
                                arr[i]=tmp
                        break    
        # it check position in 1,3,5,... order
        else:
        
            #check for positive number
            if arr[i]<0:

                for j in range(i,n):
                
                    #check for negative number
                    if arr[j]>0:

                        #store closest positive number in tmp variable
                        tmp = arr[j]

                        # left rotate array
                        for k in range(j,i,-1):
                            arr[k] = arr[k-1]
                            if k==i+1:
                                arr[i]=tmp
                                
                        break
    return arr
