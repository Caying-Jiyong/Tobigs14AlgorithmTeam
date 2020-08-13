N, W = map(int, input().split())
items = []
for n in range(N):
    name, cost, value = input().split()
    items.append([name, int(cost), int(value)])

memo = [[0 for i in range(N+1)] for j in range(W+1)]
bag = []


for w in range(W+1) :
    for i in range(N-1, -1, -1) :
        if items[i][1] <= w :
            memo[w][i] = items[i][2] + memo[w-items[i][1]][i+1]
        else :
            memo[w][i] = memo[w-1][i]
        if memo[w][i] < memo[w][i+1] :
            memo[w][i] = memo[w][i+1]
        else :

i=0
j = W
while i < N :
    if memo[j][i] != memo[j][i+1] :
        bag.append(items[i][0])
        j -= items[i][1]
    i+=1
print(memo[W][0], len(bag))
for item in bag:
    print(item)
