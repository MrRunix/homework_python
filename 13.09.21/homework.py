import random

def gen_list(num, mini, maxi):
    i = 0
    while i < num:
        yield random.randrange(mini, maxi)
        i += 1
    
print(gen_list(10, 1, 10))