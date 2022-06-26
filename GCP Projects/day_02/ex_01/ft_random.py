import random 

def get_random(n):
    return [random.randint(1,400) for x in range(0,n)]



print(get_random(6))
