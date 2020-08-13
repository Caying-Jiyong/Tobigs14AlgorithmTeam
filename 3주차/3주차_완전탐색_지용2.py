N1 = 5
codes1 = [['a',str(12)], ['b','1'], ['c','2'], ['d','3'], ['e','23']]

case1 = str(123)

N2 = 2
codes2 = [['o','10'], ['x','1']]

case2 = str(1010101)

def dfs(case, codes, decodes, decoded) :
    if case == "" :
        if decoded != "":
            tmp = "".join(decoded)
            if tmp not in decodes :
                decodes.append(tmp)
        return decodes
    for code in codes :
        if case[0] == "0":
            decoded.append("")
            decodes = dfs(case[1:], codes, decodes, decoded)
        elif code[1] == case[0:len(code[1])]:
            decoded.append(code[0])
            decodes = dfs(case[len(code[1]):], codes, decodes, decoded)
        else :
            decoded.append("")
        if len(decoded) != 0:
            decoded.pop()
    return decodes

ans = dfs(case1, codes1, [], [])
print(ans)
ans = dfs(case2, codes2, [], [])
print(ans)
