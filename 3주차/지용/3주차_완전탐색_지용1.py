import math

def ans(a,b,c) :

    candidate = []
    
    for i in range(1, int(math.sqrt(10000))+1):
        if i == a-2 or i > b or i*i >= c :
            break
        for j in range(1, int(math.sqrt(10000-i*i))+1):
            if i+j == a-1 or i*j > b or i*i + j*j > c :
                break
            for k in range(1, int(math.sqrt(10000-i*i-j*j))+1):
                if i+j+k == a and i*j*k == b and i*i+j*j+k*k == c :    
                    return i, j, k
                elif i+j+k == a or i*j*k > b and i*i+j*j+k*k > c :
                    break

    return 0, 0, 0
    
print(ans(1,2,3))
print(ans(6,6,14))
print(ans(102, 5000, 5004))
