import copy

def bfs(tmp, start):
    k = 0
    now = [start]
    while k<w+h :
        nxt = []
        for n in now :
            i = n[0]
            j = n[1]
            if [i,j] in dirty :
                start = [i,j]
                dirty.remove([i,j])
                return k, start
            if i!=0:
                if not tmp[i-1][j] :
                    nxt.append([i-1,j])
                    tmp[i-1][j] = True
            if i!=h-1:
                if not tmp[i+1][j] :
                    nxt.append([i+1,j])
                    tmp[i+1][j] = True
            if j!=0:
                if not tmp[i][j-1] :
                    nxt.append([i,j-1])
                    tmp[i][j-1] = True
            if j!=w-1:
                if not tmp[i][j+1] :
                    nxt.append([i,j+1])
                    tmp[i][j+1] = True
        now = nxt.copy()
        
        k += 1
        
    return -1, start
room = []
w, h = map(int, input().split())
for i in range(h) :
    room.append(list(input()))
"""
w, h = 7, 5
room = [['.', '.', '.', '.', '.', '.', '.'],
        ['.', 'o', '.', '.', '.', '*', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '*', '.', '.', '.', '*', '.'],
        ['.', '.', '.', '.', '.', '.', '.']]
"""

start = [0,0]
dirty = []
step = 0
visited = [[False for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        if room[i][j] == "o" :
            start = [i,j]
        elif room[i][j] == "*" :
            dirty.append([i,j])
        elif room[i][j] == "x" :
            visited[i][j] = True

m = len(dirty)
cleaned = 0
flag = False



while cleaned != m :
    copy_vi = copy.deepcopy(visited)
    copy_vi[start[0]][start[1]] == True
    count, start = bfs(copy_vi, start)

    if count == -1 :
        step = count
        break
    
    step += count
    cleaned += 1
print(step)
