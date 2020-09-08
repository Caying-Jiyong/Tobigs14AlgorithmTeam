m, k = map(int, input().split())
books = map(int, input().split())
books = list(books)
l = books[0]
u = sum(books)*2

while l+1 < u :
    ans = ""
    max_pages = 0
    pages = 0
    t = (l+u)//2
    #print(l, u, t)
    sep = k
    for i in range(m-1,-1,-1):
        if sep == 1 :
            pages += sum(books[0:i])
            max_pages = max(max_pages, pages)
        elif i == sep-1:
            pages += books[i]
            max_pages = max(max_pages, pages)
            ans = str(books[i]) + " " + ans
            #print(books[i], end=" ")
            for _ in range(i-1,-1,-1) :
                ans = str(books[_]) + " / " + ans
                #print("/", books[_], end=" ")
            break
        elif pages + books[i] >= t :
            max_pages = max(max_pages, pages)
            ans = "/ " + ans
            #print("/", end=" ")
            sep -= 1
            pages = books[i]
        else :
            pages += books[i]
        max_pages = max(max_pages, pages)
        ans = str(books[i]) + " " + ans
        #print(books[i], end=" ")
        
        
    if max_pages >= t :
        l = t
    else :
        u = t
    #print("\t",max_pages)
print(ans)
