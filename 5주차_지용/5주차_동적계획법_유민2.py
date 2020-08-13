import sys

n = int(sys.stdin.readline().rstrip())

MAX = 100
memo = [[-1 for i in range(MAX*3+1)] for j in range(MAX*3+1)]
circle = [[0 for i in range(MAX*3+1)] for j in range(MAX*3+1)]
left = 100
right = 0

it = 0
for i in range(n):
    c, r = map(int, sys.stdin.readline().rstrip().split())
    c += MAX-1
    circle[c-r][c+r] = 1
    left = min(left, c-r)
    right = max(right, c+r)

def dp(left, right) :
    #print(left, right, end=" ")
    global it
    it += 1
    if left+1 == right :
        return 0
    
    if memo[left][right] >= 0:
        return memo[left][right]

    count = circle[left][right]
    
    
    for i in range(left+1, right) :
        count = max(count, circle[left][right] + dp(left,i) + dp(i,right))

    #print(left, right, 'end', count)
    memo[left][right] = count
    return count

print(n - dp(0, 300))
