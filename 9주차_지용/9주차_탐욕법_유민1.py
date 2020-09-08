n = int(input())
works = []
due = 0
for _ in range(n):
    d, w = map(int, input().split())
    due = max(due, d)
    works.append([d,w])
works = sorted(works, key = lambda x : -x[1])
result = 0
for i in range(due, 0, -1):
    for work in works :
        if work[0] >= i :
            result += work[1]
            #print(i, work, result)
            works.remove(work)
            break
print(result)
