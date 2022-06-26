

def gen_tuples(start,end):
    return [(t,x) for x in range(start,end+1) for t in range(x,0,-1)]



print(gen_tuples(2,4))