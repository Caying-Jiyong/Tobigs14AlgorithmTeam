N = 5
minemap = [[1,1,1,0,0],
           [2,'*','*','*', 1],
           [3,'*','*','*', 1],
           [2,'*','*','*', 1],
           [1,2,2,1,0]]
           

def minecounter(N, minemap):
    mine = 0
    if minemap[0][0] == 1 :    #왼쪽위 귀퉁이
        mine += 1
        minemap[0][0] -= 1
        if N > 1 :
            minemap[0][1] -= 1
            minemap[1][0] -= 1
        if N > 2 :
            minemap[0][2] -= 1
            minemap[2][0] -= 1
    if minemap[N-1][0] == 1 :   #왼쪽아래 귀퉁이
        mine += 1
        minemap[N-1][0] -= 1
        if N > 1 :
            minemap[N-1][1] -= 1
            minemap[N-2][0] -= 1
        if N > 2 :
            minemap[N-1][2] -= 1
            minemap[N-3][0] -= 1
    if minemap[0][N-1] == 1 :   #오른쪽위 귀퉁이
        mine += 1
        minemap[0][N-1] -= 1
        if N > 1 :
            minemap[0][N-2] -= 1
            minemap[1][N-1] -= 1
        if N > 2 :
            minemap[0][N-3] -= 1
            minemap[2][N-1] -= 1
    if minemap[N-1][N-1] == 1 :   #오른쪽아래 귀퉁이
        mine += 1
        minemap[N-1][N-1] -= 1
        if N > 1 :
            minemap[N-1][N-2] -= 1
            minemap[N-2][N-1] -= 1
        if N > 2 :
            minemap[N-1][N-3] -= 1
            minemap[N-3][N-1] -= 1
    print(minemap)

    if N > 4 :
        for i in range(1, N-3):
            if minemap[0][i] > 0 : #윗줄
                mine += 1
                minemap[0][i] -= 1
                minemap[0][i+1] -= 1
                minemap[0][i+2] -= 1
            if minemap[N-1][i] > 0 : #아랫줄
                mine += 1
                minemap[N-1][i] -= 1
                minemap[N-1][i+1] -= 1
                minemap[N-1][i+2] -= 1    
        for i in range(1, N-2):
            if minemap[i][0] > 0 :   #왼쪽줄
                mine += 1
                minemap[i][0] -=1
                minemap[i+1][0] -=1
                minemap[i+2][0] -=1
            if minemap[i][N-1] > 0 :   #오른쪽줄
                mine += 1
                minemap[i][N-1] -=1
                minemap[i+1][N-1] -=1
                minemap[i+2][N-1] -=1
        mine += (N-4)*(N-4)
    print(mine)
    return mine


minecounter(N, minemap)






            
            
