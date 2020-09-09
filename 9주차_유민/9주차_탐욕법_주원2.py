# ID y305205 참고

import queue

N = int(input())
L = []
ans = 0

for i in range(N):
    x,y = map(int,input().split())
    L.append((-y,x))
pq = queue.PriorityQueue()
L.sort()

idx = 0
for day in range(1,12345)[::-1]:
    while idx < N and -L[idx][0] >= day:
        pq.put(-L[idx][1])
        idx+= 1
    if pq.qsize():
        ans-= pq.get()
        
print(ans)

