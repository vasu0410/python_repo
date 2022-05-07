'''For an array, inversion count indicates how far (or close) the array is from being sorted. If array is 
   already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count 
   is the maximum. Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
   
   Test Case 1:

        Input: arr[] = {2, 4, 1, 3, 5}
        Output: 3
    
        Explanation: The sequence 2, 4, 1, 3, 5 
        has three inversions (2, 1), (4, 1), (4, 3).
    
    Test Case 2:

        Input: arr[] = {2, 3, 4, 5, 6}
        Output: 0
    
        Explanation: As the sequence is already 
        sorted so there is no inversion count.
    
    Test Case 3:

        Input: arr[] = {10, 10, 10}
        Output: 0
    
        Explanation: As all the elements of array 
        are same, so there is no inversion count.
    '''

def count_inversion(arr):
        '''
        count : to store inversion count
        n : store length of arr
        arr : input array
        '''
        count = 0
        n = len(arr)
        
        #for loop of i in range of array length and j in range i+1 element to length of array
        for i in range(n):
            for j in range(i+1,n):
                
                # array i'th element is geater than array j'th elment count inversion as + 1
                if arr[i] > arr[j]:
                    count +=1
        return count
