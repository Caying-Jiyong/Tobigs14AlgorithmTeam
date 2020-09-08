n = int(input())
coin = map(int, input().split())
coin = sorted(list(coin))
sum = 1
count = 0
if len(coin) > 1 :
    count = 2
else :
    count = 1
for i in range(1, len(coin)-1) :
    if sum + coin[i] <= coin[i+1] :
        sum += coin[i]
        count += 1
print(count)
###
