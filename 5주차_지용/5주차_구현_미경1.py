def num(n) :
    ans = ""
    while n>=20:
        ans += str(n%10)
        n = n//10
    if n>10 :
        ans += str(n%10)
        ans = ans[::-1]+ans
    else :
        ans += str(n-1)
        if len(ans)>1 :
            ans = ans[1:][::-1]+ans
    return int(ans)
