N = 4
forest = [[14,9,12,10],
          [1,11,5,4],
          [7,15,2,13],
          [6,3,16,8]]
survive = [[1 for i in range(N)] for i in range(N)]


t = 1
flag = True
while t <= N*N and flag:
    flag = False
    for i in range(N) :
        for j in range(N) :
            if i != 0 and forest[i-1][j] > forest[i][j] and survive[i-1][j] >= survive[i][j]:
                survive[i][j] += 1
                if not flag :
                    flag = True
                break
            if i != N-1 and forest[i+1][j] > forest[i][j] and survive[i+1][j] >= survive[i][j]:
                survive[i][j] += 1
                if not flag :
                    flag = True
                break
            if j != 0 and forest[i][j-1] > forest[i][j] and survive[i][j-1] >= survive[i][j]:
                survive[i][j] += 1
                if not flag :
                    flag = True
                break
            if j != N-1 and forest[i][j+1] > forest[i][j] and survive[i][j+1] >= survive[i][j]:
                survive[i][j] += 1
                if not flag :
                    flag = True
                break

    print(survive)

    t += 1

ans = 0
for i in range(N):
    ans = max(max(survive[i]), ans)

print(ans)    
