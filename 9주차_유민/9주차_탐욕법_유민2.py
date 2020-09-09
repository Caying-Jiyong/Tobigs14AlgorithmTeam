N = int(input())
cost = list(map(int, input().split()))
ans = ['0']*(int(input())+1)

for i in range(N)[::-1]:
    c = cost[i]

    for b in range(c, len(ans)):
        ans[b] = ans[b-c]+str(i) if int(ans[b]) <= int(ans[b-c]+str(i)) else ans[b]

print(int(ans[-1]))

