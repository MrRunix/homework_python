import random

glas=['a','e','y','u','i','o']
sogl=['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
clan=['uchiha','uzumaki','hyuuga','hatake']

def generation_name(glas,sogl,num):
    i = 1
    while i < num :
        name = ''
        name += random.choice(clan) + ' '
        for x in range(0, 3):
            name += random.choice(sogl)
            name += random.choice(glas)

        yield name
        i += 1
for name in generation_name(glas,sogl,5):
    print(name)