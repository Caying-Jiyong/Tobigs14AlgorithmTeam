import copy

def bfs(n):
    #n = int(input())
    visited = [n]
    nxt = [n]
    count = 0
    while 1 not in nxt :
        count += 1
        tmp = []
        for k in nxt :
            if k-1 not in visited :
                tmp.append(k-1)
                visited.append(k-1)
            if k%2 == 0 and k//2 not in visited :
                tmp.append(k//2)
                visited.append(k//2)
            if k%3 == 0 and k//3 not in visited :
                tmp.append(k//3)
                visited.append(k//3)
        nxt = copy.deepcopy(tmp)
    return count

print(bfs(2))
print(bfs(50000))
