def dice():
    yes = 'yes'
    no = 'no'
    dev = []
    rows = [0 for i in range(6)]
    cols = [0 for i in range(6)]
    tmpr = []
    tmpc = []

    for i in range(6) :
        dev.append([int(x) for x in list(input().split())])
    for i in range(6) :
        for j in range(6):
            if dev[i][j] == 1:
                rows[i] += 1
                cols[j] += 1
                
    for i in range(6) :
        if rows[i] != 0 :
            tmpr.append(rows[i])
        if cols[i] != 0 :
            tmpc.append(cols[i])

    if tmpr == [1,4,1] or tmpc == [1,4,1] :
        print(yes)
    elif tmpr in [[1,3,2], [2,3,1]] :
        if tmpc in [[1,3,1,1], [1,1,3,1], [1,2,2,1], [2,1,2,1], [1,2,1,2]] :
            print(yes)
        else :
            print(no)
    elif tmpc in [[1,3,2], [2,3,1]] :
        if tmpr in [[1,3,1,1], [1,1,3,1], [1,2,2,1], [2,1,2,1], [1,2,1,2]] :
            print(yes)
        else :
            print(no)
    elif tmpr == [2,2,2]:
        if tmpc == [1,2,2,1]:
            print(yes)
        else :
            print(no)
    elif tmpc == [2,2,2]:
        if tmpr == [1,2,2,1]:
            print(yes)
        else :
            print(no)
    elif tmpr == [3,3]:
        if tmpc == [1,1,2,1,1]:
            print(yes)
        else :
            print(no)
    elif tmpc == [3,3]:
        if tmpr == [1,1,2,1,1]:
            print(yes)
        else :
            print(no)
    else :
        print(no)
dice()
