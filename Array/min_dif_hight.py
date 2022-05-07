'''Find out the minimum possible difference of the height of shortest and longest 
    towers after you have modified each tower.
    
    Test Case 1:
        
        input = [1, 5, 8, 10] , 2 (value of hights)
        output = 5

        explanation :
        The array can be modified as {3, 3, 6, 8}. The difference between 
        the largest and the smallest is 8-3 = 5.

    Test Case 2:
        
        input = [8 ,1 ,5 ,4 ,7 ,5 ,7 ,9 ,4 ,6] , 5
        output = 8

        invelid :
        output = 7
        
        explanation:
        k_hight value always positive,negative number not include in minimum difference between hights.

    '''

def min_hight(arr,k):
    '''
    arr : input array
    k  : add or remove k hight to every element to minimize difference
    maxx : to store maximum value from array element
    minn : to store minimum value from array element
    ans : to store difference between last and first element before changing hights
    n : length of array
    '''

    # sorting array
    arr.sort()

    #store array last element to maxx and first element to minn
    maxx = arr[-1]
    minn = arr[0]

    # store difference before modifing array
    ans  = maxx-minn
    n = len(arr)

    for i in range(1,n):

        #skip loop if element-k is negative number
        if arr[i]-k<0:
            continue

        #add k hight to every element and compare with last element - k hight
        #and find max value and store to maxx
        maxx = max(arr[i-1]+k,arr[n-1]-k)

        #add k hight to first element and compare with every element - k hight
        #and store min value to minn
        minn = min(arr[0]+k,arr[i]-k)

        #store minimum value of ans value and maxx-minn value
        ans = min(ans,maxx-minn)


    return ans


