N1 = 5
codes1 = [['a',str(12)], ['b','1'], ['c','2'], ['d','3'], ['e','23']]

case1 = str(123)

N2 = 2
codes2 = [['o','10'], ['x','1']]

case2 = str(1010101)

decoded = ""
def decode(case, codes, decoded):
    decodes = []
    for code in codes :
        if case[0:len(code[1])] == code[1] :
            decoded = decoded + code[0]
            print(decoded)
            if len(case) == len(code[0]) :
                decodes.append(decoded)
            else:
                tmps = decode(case[len(code[1]):], codes, decoded)
            print(tmps)
    return decodes

print(decode(case1, codes1, decoded))
print(decode(case2, codes2, decoded))
