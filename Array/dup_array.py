''' Given an array of integers nums containing n + 1 integers 
    where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array 
    nums and uses only constant extra space.
    
    Test Case 1:
        input = [3,1,3,4,2]
        ouput = 3
        
    Test Case 2:
        input = [1,3,4,2,2]
        output = 2    
    '''


def duplicate_arr(nums):
    '''
    nums : input array
    '''

    for i in range(len(nums)):
        for j in range(len(nums)):
            
            # if value of i is equal to j than skip the loop
            if i==j:
                continue

            # check value is repeated or not
            if nums[i]==nums[j]:
                
                return nums[i]
                