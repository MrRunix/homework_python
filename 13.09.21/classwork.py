import random
#n = random.randint(0 , 100)
a = []
for i in range(random.randrange(0, 30)):
    a.append(random.randrange(0, 100))
#for i in range(n+1):
#    a.append(i)

def sortir(list):
    t = 1
    while t != 0:
        i = 0
        for i in range(len(list)):
            t = 0
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
                t += 1
        print(list)
        print(t)
    return list
 
print(a)
print(sortir(a))


