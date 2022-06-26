def gen_dict():
    return {str(16-key):value+key-2  for key in range (15,1,-1) for value in range(22,8,-1)}

print(gen_dict())