def walk(n, m) :
    if n == m :
        return 0
    elif n > m :
        return n-m
    else :
        return jump(n*2, m) + 1

def jump(n, m) :
    if n == m :
        return 0
    elif n > m :
        return n-m
    else :
        a = walk(n+1, m) + 1
        b = 10000
        if n > 1 :
            b = walk(n-1, m) + 1
        if n*2 > m :
            c = min(m-n, 2*n-m+1)
        else :
            c = jump(n*2, m) + 1
        return min(a,b,c)

ans = jump(4, 102)
print(ans)
