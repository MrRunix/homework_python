name ='serg astr kons'
def fio(name):
    g=0
    result=[]
    for i in range(len(name)):
        if name[i]==' ':
            result.append(name[g:i])
            g=i+1
        if i == len(name)-1:
            result.append(name[g:i])
    return result[0] + ' ' + result[1][0:1] + '. ' + result[2][0:1] + '.'
print(fio(name))

names ='serg astr kons, gong gim git, rod fitter gib'
def fio(name):
    l = name.split()
    return l[0] +' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'
def fios(name):
    res=[]
    #for i in range(names.count(",")+1):
    for name in names:
        nname=fio(name)
        res.append(nname)
    return res