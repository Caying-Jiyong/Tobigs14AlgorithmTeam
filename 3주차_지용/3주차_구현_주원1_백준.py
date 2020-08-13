import sys
input = sys.stdin.readline

N = int(input())
forest = []
for i in range(N):
    forest.append(list(map(int, sys.stdin.readline().split())))

survive = [[0 for i in range(N)] for j in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def canmove(x, y) :
    return (x >= 0 and x< N and y >= 0 and y < N)

def dp(x, y) :
    if survive[x][y] != 0 :
        return survive[x][y]
    else :
        tmp = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if canmove(nx,ny) and forest[x][y] < forest[nx][ny] :
                tmp = max(tmp, dp(nx,ny)+1)
        survive[x][y] = tmp
        return survive[x][y]
ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dp(i,j))
print(ans)
