'''Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the 
    subsequence are consecutive integers, the consecutive numbers can be in any order.
 
    Test Case 1:

    Input   : {2,6,1,9,4,5,3}
    Output  : 6

    Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest 
                 consecutive subsquence.

    Test Case 2:

    Input   : {1,9,3,10,4,20,2}
    Output  : 4

    Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.'''


def con_squence(arr):
        
        '''
        ans : to store length of longest consecutive subsequence
        arr : input array
        tmp : to store temp element
        count : to store count consecutive subsequence
        '''

        ans = 0
        arr = set(arr)
        arr = list(arr)
        arr.sort()
        tmp = arr[0]
        count = 1
        
        # if arr length is 1 than output 1
        if len(arr)==1:
            return 1
        

        for i in range(1,len(arr)):
            
            # check consecutive subsequence using tmp value and increase count 
            if tmp+1 == arr[i]:
                count += 1
                tmp = arr[i]

            # if subsequence not found reset the count and store new element value to tmp     
            else:
                count = 0
                tmp = arr[i]
                count +=1
            
            # return max length of sequence
            ans = max(count,ans)

        return ans
