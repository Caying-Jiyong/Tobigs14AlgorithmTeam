x = []
N = int(input())

for i in range(N):
	c, d = map(int, input().split())
	x.append((c, d))

x.sort(key=lambda y : (-y[1]))
day = [0 for i in range(1004)]

ans = 0
for d, s in x:
	while d > 0:
		if day[d] == 0:
			day[d] = 1
			ans += s
			break
		d -= 1

print(ans)