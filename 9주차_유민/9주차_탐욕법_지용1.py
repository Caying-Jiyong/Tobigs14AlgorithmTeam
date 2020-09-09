N = int(input())
 
for _ in range(N):
    total = int(input())
    rus = list(map(int, input().split()))
    kor = list(map(int, input().split()))
    win = 0
    
    # rus 내림차, kor 오름차 정렬 후 높은 rating끼리 비교
    rus.sort(reverse=True) 
    kor.sort()
 
    for i in range(total):
        if rus[i] > kor[-1]:
            continue
        # kor >= rus 인 경우 kor의 rating 제거 + 경우의 수 1 증가
        else:
            kor.pop()
            win += 1
 
    print(win)

