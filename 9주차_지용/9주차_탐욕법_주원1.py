from copy import deepcopy 

n = int(input())
m = int(input())
A = []
B = []
minB = n
maxB = 0
for i in range(1, m+1) :
    start, end = map(int, input().split())
    if start < end :
        A.append([i,start,end])
    else :
        B.append([i,start,end])
        minB = min(minB, start)
        maxB = max(maxB, end)
A = sorted(A, key = lambda x : (x[1], -x[2]))
B = sorted(B, key = lambda x : (x[1], -x[2]))
#print(A,B)
tmpA = []
e = 0
for a in A :
    if a[2] > e :
        tmpA.append(a)
        e = a[2]
A = tmpA
#print(A)
#print(maxB, minB)
result = []
for a in A :
    if a[1] < minB and a[2] > maxB:
        result.append(a[0])
e=B[0][2]
result.append(B[0][0])
for b in B :
    if b[2] > e :
        result.append(b[0])
        e = b[2]
print(*sorted(result))
