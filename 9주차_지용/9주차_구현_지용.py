#m = int(input())
#n = int(input())

m, n = 3, 3
city_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
"""
m, n = 3, 6
city_map = [[0, 2, 0, 0, 0, 2],
            [0, 0, 2, 0, 1, 0],
            [1, 0, 0, 2, 2, 0]]
"""
dp = [[0 for j in range(n)] for i in range(m)]
dp[0][0] = 1
for i in range(m) :
    for j in range(n) :
        if i != 0 :
            dp[i][j] += dp[i-1][j]
        if j != 0 :
            dp[i][j] += dp[i][j-1]
        if city_map[i][j] == 1 :
            dp[i][j] = 0
        elif city_map[i][j] == 2:
            if i != m-1 :
                dp[i+1][j] -= dp[i][j-1]
            if j != n-1 :
                dp[i][j+1] -= dp[i-1][j]
        
print(dp[m-1][n-1])
