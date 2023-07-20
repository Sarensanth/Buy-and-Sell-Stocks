def buy_and_sell(array):

    profit=0
    for i in range(len(array)-1):
        profit=max(profit,max(array[i+1::])-array[i])
    return profit
    
array=list(map(int,input().split()))
print(buy_and_sell(array))
