#n, k = map(int, input().split())

def combi(n,k) :
    ans = 1
    for i, j in zip(range(n+1, n+k), range(1,k)) :
        ans *= i
        ans /= j
    return int(ans)

print(combi(20, 2))
        
def dp(n,k):
    memo = [1 for i in range(n+2)]
    for a in range(1, k):
        tmp = []
        for b in range(n+1):
            tmp.append(sum(memo[0:b+1]))
        memo = tmp
        print(memo)
    return memo[-1]
print(dp(20,3))
