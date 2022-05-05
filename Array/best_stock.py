''' You are given an priceay prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
    in the future to selaxxhat stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, 
    return 0
    
    Test Case 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5

    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Test Case 2:

    Input: prices = [7,6,4,3,1]
    Output: 0

    Explanation: In this case, no transactions are done and the max profit = 0.'''


def best_profit(price):
    '''
    min_price : have the minimum price value to calculate profit
    max_profit : to store maximum price value for profit
    n    : to store length of price array
    '''

    # min_price value is first price of array and max value is 0 which applicable on 
    # all price>=0
    min_price = price[0]
    max_profit = 0
    n = len(price)
    
    for i in range(n):
        
        # store min prices to calculate profit
        min_price = min(min_price,price[i])

        # compare max_profit with price of i'th element - min_price value and store max profit 
        max_profit = max(max_profit,price[i]-min_price)        

    return max_profit


