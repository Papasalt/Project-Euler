def P31(n, coins):
    ways = [[1]+[0 for _ in range(0,n)] for _ in range(0,len(coins))]
    init = coins[0]
    for a in range(1,n+1):
        if a % init == 0:
            ways[0][a] = 1
    
    for coin in range(1,len(coins)):
        c = coins[coin]
        for a in range(1,n+1):
            ways[coin][a] = ways[coin-1][a]
            ways[coin][a] += ways[coin][a-c]
            
    return ways[-1][-1]

print(P31(200, [1,2,5,10,20,50,100,200]))