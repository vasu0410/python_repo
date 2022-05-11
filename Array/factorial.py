'''Given an integer N, find its factorial.

    Test Case 1:

        Input: N = 5
        Output: 120

        Explanation : 5! = 1*2*3*4*5 = 120
 
    Test Case 2:

    Input: N = 10
    Output: 3628800
    
    Explanation : 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800'''

def fact(N):
    if N<=1:
        return 1

    else:
        return N*fact(N-1)


N = 10
print(fact(N))



