cost = map(int, input().split())
cost = list(cost)

profit = 0
for i in range(len(cost)-1):
    profit = max(profit, max(cost[i+1:])-cost[i])
print(profit)
