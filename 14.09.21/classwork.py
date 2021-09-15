import string
d = {'reg' : 23 , 'ege' : 17, 'favor' : 11}
d1 = {}
d1['ege'] = 18
d1['colleague'] = 75

def value(d, k):
    if k in d.keys():
        return d[k]
    else:
        return -1

def value_02(d, k):
    return d.get(k, -1)
#print(value_02(d, 'reg'))

d.update(d1)
#print(d.items())

di = {}
def ascii_upper(di):
    di = {}
    for  i in range(65,91):
        di[chr(i)] = i
    return di
#print(ascii_upper(di))


def counter_letters(s): 
    di = {}
    k = string.ascii_lowercase
    for i in range(len(k)):
        di[k[i]] = s.count(k[i])
    return di
#print(counter_letters('aaaaaaa'))


def creat_city(p, s):
    return{'population' : p,
           'size' : s}
def creat_region(names, cities):
    d = { }
    for name,city in zip(names,cities):
        d[name] = city
    return d

names = [ ]
cities = [ ]
i = 0
while i < 3:
    name = input('введите название города - ')
    population = input('введите население - ')
    size = input('введите размер - ')
    cities.append(creat_city(population,size))
    names.append(name)
    i +=1
    print(cities)
    print(names)


def sort(x):
    return sorted(x, key = lambda x:x[1])


key = {'key1' : 5,
     'key2' : 2,
     'key3' : 8,
     'key4' : 1}
x = key.items()

print(sort(x))