def triangle(lines):
    grads = dict()
    for line in lines :
        grad = line[0]/line[1]
        if grad not in grads :
            grads[grad] = set()
        grads[grad].add(-line[2]/line[1])

    
    grads_key = list(grads.keys())
    line_num = len(grads[grads_key[0]])
    tris = 0
    dots = 0
    for i in range(1, len(grads_key)) :
        tris += dots*len(grads[grads_key[i]])
        dots += line_num
        line_num += len(grads[grads_key[i]])
    return tris
        
        
lines = [[0,1,0], [-5,3,0],[-5,-2,25],[0,1,-3],[0,1,-2],[-4,-5,29]]
print(triangle(lines))
