N = int(input())
grads = {}
mod = 1000000007
ans = 0

for n in range(N):
    grad = 0
    a, b, c = map(int, input().split())
    if b == 0 :
        grad = float('inf')
    else :
        grad = a/b
    if grad not in grads :
        grads[grad] = 1
    else :
        grads[grad] += 1

val = grads.values()
if len(val) > 2 :
    num_line = sum(val)
    A = num_line**3
    B = sum(i**2 for i in val) * num_line
    C = sum(i**3 for i in val)
    ans = (A-3*B+2*C//6)
if len(grads.keys()) < 3:
    ans = 0

print(ans%mod)
