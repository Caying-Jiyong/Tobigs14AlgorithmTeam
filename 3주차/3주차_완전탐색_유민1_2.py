# 가정 : 0 < N < 100000

def time(x):
    visited = [False]*100001
    visited[x] = True
    q = [x]
    q_nxt = []
    count = 0

    while q:
        if M in q :
            print(count)
            break
        for x in q:
            if x-1 > 0 and not visited[x-1]:
                q_nxt.append(x-1)
                visited[x-1] = True
            if x+1 <= 100000 and not visited[x+1]:
                q_nxt.append(x+1)
                visited[x+1] = True
            if x*2 <= 100000 and not visited[x*2] :
                q_nxt.append(x*2)
                visited[x*2] = True

        q = q_nxt.copy()
        q_nxt = []
        
        print(q)
        count+=1

N, M = map(int, input().split())  # 초기위치

time(N) #최단시간
