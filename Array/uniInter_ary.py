''' write a program to find the Union and Intersection of the two sorted arrays

    Test Case 1

        input1 = [1,2,3,4,5]
        input2 = [1,2,4]
    
        output = 5(union value) 3(Intersection)
    or
        output = 3(Intersection) 5(union value)   

    Test case 2

        input1 = [85,25,1,32,54,6]
        input2 = [85,2]
        output = 7 1
'''

def union_array(a1,a2):
    '''
    a1 : input array1
    a2 : input array2
    tmp : temp variable to store union of array
    '''
    #convert list into type set to use inbuilt function 
    a1 = set(a1)
    a2 = set(a2)

    #use union function on set1 and set2 
    tmp = a1.union(a2)

    # return lenength of tmp variable becuase tmp store union of array 1 and 2
    return len(tmp)

def itersection_array(a1,a2):
    '''
    a1 : input array1
    a2 : input array2
    tmp : temp variable to store intersection of array
    '''
    #convert list into type set to use inbuilt function 
    a1 = set(a1)
    a2 = set(a2)    
    
    #use intersecion function set1 and set2
    tmp = a1.intersection(a2)

    # return lenength of tmp variable becuase tmp store union of array 1 and 2
    return len(tmp)




