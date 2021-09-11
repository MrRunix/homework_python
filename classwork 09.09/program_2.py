names =['serg astr kons', 'gong gim git', 'rod fitter gib']
def fio(name):
    l = name.split()
    return l[0] +' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'
def fios(names):
    #return [fio(name) for name in names]
    res=[]
    #for i in range(names.count(",")+1):
    for name in names:
        nname=fio(name)
        res.append(nname)
    return res

print(fios(names))