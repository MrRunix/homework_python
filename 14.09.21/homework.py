def creat_city(p, s):
    return{'population' : p,
           'size' : s}

names = [ ]
cities = [ ]
i = 0

while True:
    name = input('введите название города - ')
    if name == 'stop':
        break
    population = input('введите население - ')
    size = input('введите размер - ')
    cities.append(creat_city(population,size))
    names.append(name)
    print(cities)
    print(names)


def sort(x):
    return sorted(x, key = lambda x:x[1])


key = {'key1' : 4,
     'key2' : 3,
     'key3' : 6,
     'key4' : 0}
x = key.items()

print(sort(x))