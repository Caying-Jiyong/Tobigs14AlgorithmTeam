t = int(input())
for test in range(t):
    n = int(input())
    rus = map(int, input().split())
    rus = sorted(list(rus))
    kor = map(int, input().split())
    kor = sorted(list(kor))
    win = 0
    for i in range(n) :
        for j in range(len(kor)):
            if rus[i]<=kor[j] :
                kor.pop(j)
                win += 1
                break
    print(win)
