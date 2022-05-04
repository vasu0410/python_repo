''' write a programe to take input array and give next possible permutation 
    
    For example, for arr = [1,2,3], the following are considered permutations of 
    arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1] 
    
    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3]

    Test Case 1:
        Input: arr = [1,2,3]
        Output: [1,3,2]

    Test Case 2:
        Input: arr = [3,2,1]
        Output: [1,2,3]

    Test Case 3:
        Input: arr = [1,1,5]
        Output: [1,5,1]
'''

def next_permutation(arr):
        '''
        arr : input array
        '''

        # if lenght of arr is 1 return input array as it is
        if len(arr) == 1:
            return arr
        
        # loop from length of arr - 2 in reverse order and end at 0 value
        for i in range(len(arr) - 2, -1, -1):
            
            # here if i'th index value is less than i+1 than go to loop block
            if arr[i] < arr[i + 1]:
                
                # simply j value start from length of arr - 1 and end at i value in reverse order
                for j in range(len(arr) - 1, i, -1):

                    # check j'th element is greater than i'th element  
                    if arr[j] > arr[i]:

                        # swape value of i'th and j'th element 
                        arr[i], arr[j] = arr[j], arr[i]

                        # sort array after i+1 element till to end of array
                        arr[i+1:] = sorted(arr[i+1:])
                        break
                break
            
            else:
                # if i value became 0 than simply sort array
                if i == 0:
                    arr.sort()
        
        return arr


