# 배열의 크기
size = int(input())

# 지뢰찾기 보드 만들기
mine = []
for _ in range(size):
	mine.append(list(input()))

# 방향: 12시부터 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 문자열을 숫자로 대체
for i in range(size):
	for j in range(size):
		if mine[i][j] == '#':
			mine[i][j] = -1
		else:
			mine[i][j] = ord(mine[i][j]) - ord('0')

num_mines = 0
# 사이즈가 3보다 작은 경우 지뢰가 없음
if size > 2:
	# 처음에 모든 좌표에 대해 지뢰가 있다고 가정 (내륙에 위치하면 무조건 지뢰가 있기 때문)
	num_mines = (size-2)*(size-2)
	# 지뢰가 있을 것 같은 부분만 확인 (외벽 제외)
	for i in range(1, size-1):
		for j in range(1, size-1):
			# 주어진 좌표 기준 지뢰가 있다고 가정
			if mine[i][j] == -1:
				flag = True
				for k in range(len(dx)):
					nx = i + dx[k]
					ny = j + dy[k]
					# 해당 칸 주위에 0이 있기에 이 칸에는 지뢰가 없음
					if mine[nx][ny] == 0:
						flag = False
						num_mines -= 1
						# 모든 방향을 검토할 필요가 없음
						break
				# 지뢰가 있는 경우 8방위 숫자에서 1을 빼기
				if flag:
					for k in range(len(dx)):
						nx = i + dx[k]
						ny = j + dy[k]
						if 0 < mine[nx][ny] < 9:
							mine[nx][ny] -= 1

print(num_mines)