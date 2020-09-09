g = [input().split() for _ in range(9)]
r = [[False] * 10 for _ in range(9)]
c = [[False] * 10 for _ in range(9)]
s = [[False] * 10 for _ in range(9)]

def sudoku(idx):
    if idx == 81:
        [print(*g[i]) for i in range(9)]
        exit(0)
    x, y = idx // 9, idx % 9
    part = (x//3)*3 + (y//3)

    if g[x][y] != '0':
        sudoku(idx + 1)
    else:
        for i in range(1, 10):
            if r[x][i] or c[y][i] or s[part][i]:
                continue

            r[x][i] = c[y][i] = s[part][i] = True
            g[x][y] = str(i)
            sudoku(idx + 1)

            g[x][y] = '0'
            r[x][i] = c[y][i] = s[part][i] = False


for i in range(9):
    for j in range(9):
        x = int(g[i][j])
        if x != 0:
            r[i][x] = c[j][x] = s[(i//3)*3 + (j//3)][x] = True

sudoku(0)

