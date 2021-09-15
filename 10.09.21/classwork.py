import string
s = string.ascii_lowercase


#l1=list(s)

#l2=[]
#for n in range(65,90):
#    l2.append(chr(n))

l = [c for c in s]

def f(l):
    for d in l:
        print(d)
#f((l)

def f2(l):
    i=0
    while i < len(l):
        print(l[i])
        i+=1

#f2(l)
def dec(leng):
    def new_leng(*args,**kwargs):
        print('Running function: ', leng.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = leng(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_leng

f2_dec = dec(f2)

f2_dec(l)