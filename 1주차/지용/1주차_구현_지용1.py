one = ['a','d','g','j','m','p','t','w',' ']
two = ['b','e','h','k','n','q','u','x', 0]
three = ['c','f','i','l','o','r','v','y', 0]
four = [0, 0, 0, 0, 0, 's', 0,'z', 0]

words1 = 'welcome to ulab'
words2 = 'good luck and have fun'

def countpress(word) :
    word = list(word)
    press = 0
    for w in word :
        if w in one :
            press +=1
        elif w in two :
            press +=2
        elif w in three :
            press +=3
        else :
            press +=4
    print(press)
    return(press)

countpress(words1)
countpress(words2)
