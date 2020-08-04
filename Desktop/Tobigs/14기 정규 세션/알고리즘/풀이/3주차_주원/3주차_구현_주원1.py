# 대나무숲에서 조건에 맞는 자리로 옮기기
def dfs(i, j):
	if flag[i][j]:
		return flag[i][j]
	# 해당 지점의 경로를 판단했다는 뜻
	flag[i][j] = 1
	# 상하좌우를 검색
	for d in range(4):
		ni, nj = i + di[d], j + dj[d]
		# 이동할 좌표가 대나무숲 안에 위치하고, 대나무의 수가 더 많다면:
		if 0 <= ni < N and 0 <= nj < N and forest[i][j] < forest[ni][nj]:
			flag[i][j] = max(flag[i][j], dfs(ni, nj)+1)
	return flag[i][j]


N = int(input())
# 대나무숲 만들기
forest = [list(map(int, input().split())) for _ in range(N)]
# 해당 좌표를 기준으로 경로를 찾았으면 1 아니면 0 (처음에는 0으로 초기화)
flag = [[0]*N for _ in range(N)]
# 상하좌우 좌표에 해당
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 모든 좌표에 대해 길 찾기
for i in range(N):
	for j in range(N):
		flag[i][j] = dfs(i, j)

# 판다가 가장 오래 살 수 있는 일수를 출력
print(max(max(flag)))