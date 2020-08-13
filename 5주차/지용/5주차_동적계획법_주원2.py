mini = {2:"1", 3:"7", 4:"4", 5:"2", 6:"6", 7:"8", 8:"10"}

n = int(input())
a = n
i = ""
j = ""
while n > 8 :
    i = mini[7] + i
    n -= 7
i = mini[n] + i

while a > 3 :
    j = mini[2] + j
    a -= 2
j = mini[a] + j


print(i, j)

