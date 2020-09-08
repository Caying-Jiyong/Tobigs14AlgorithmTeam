#L = [7,2,1,4,5,1,3,3]
#N = L.pop(0)

ans = 0
def square(left, right) :
    if left == right :
        return L[left]
    mid = (left+right)//2
    #print(left, right, mid)
    lo = mid
    hi = mid+1

    ans = max(square(left, mid), square(mid+1, right))

    height = min(L[lo], L[hi])
    ans = max(ans, height*2)
    
    while left < lo or right > hi :
        if hi < right and (lo == left or L[lo-1] < L[hi+1]) :
            hi += 1
            height = min(height, L[hi])
        else :
            lo -= 1
            height = min(height, L[lo])


        ans = max(ans, height*(hi-lo+1))
                  
    return ans
while True :
    L = list(map(int, input().split()))
    N = L.pop(0)
    if N == 0 :
        break
    ans = square(0, len(L)-1)
    print(ans)
