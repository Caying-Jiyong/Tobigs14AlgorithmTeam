def logger(N, C, W, woods) :
    money = 0
    for i in range(1, min(woods)+1) :
        cut = 0
        tmp = 0
        for wood in woods :
            cut += (wood - 1)//i
            tmp += (wood-wood%i)*W
        tmp -= cut*C
        if tmp > money:
            money = tmp
        print(i, tmp, cut)
    print(money)
    return money

logger(3, 1, 10, [26,103,59])
