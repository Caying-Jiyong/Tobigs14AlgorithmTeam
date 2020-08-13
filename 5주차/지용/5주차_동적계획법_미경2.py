import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

class Node:
    def __init__(self, data, parent) :
        self.data = data
        self.parent = parent
        self.degree = 1
        self.children = []
    def info(self):
        print(self.data, self.parent, self.degree, self.children)
    

def get_nodes():
    N = int(input())
    M = int(input())
    records = []
    
    root = Node(0,0)
    root.degree = 0
    nodes = [root]

    for i in range(1, N+1):
        nodes.append(Node(i, 0))
        nodes[0].children.append(i)
    for m in range(M):
        i,j = map(int, input().split())
        if [j,i] in records :
            print(2)
        else :
            records.append([i,j])
    for record in records :
        i = record[0]
        j = record[1]
        if nodes[j].degree <= nodes[i].degree :
            if j in nodes[nodes[j].parent].children:
                nodes[nodes[j].parent].children.remove(j)
            nodes[j].parent = i
            nodes[i].children.append(j)
            nodes[j].degree = nodes[i].degree+1
    return nodes

def comb(idx, nodes):
    counts = []
    node = nodes[idx]
    #node.info()
    if len(node.children) == 0 :
        return [1, 1]       #개수, 경우의수
    for child in node.children :
        print("child:", child)
        counts.append(comb(child, nodes))
    print(idx, counts)
    if len(counts) == 1:
        return [counts[0][0]+1, counts[0][1]]
    else :
        num = counts[0][0]
        count = counts[0][1]
        for i in range(1, len(counts)):
            n = counts[i][0]
            count *= ncr(n+num,n)*counts[i][1]
            num += n
            
    return [num+1, count]

    
nodes = get_nodes()
print(comb(0, nodes)[1])
        

