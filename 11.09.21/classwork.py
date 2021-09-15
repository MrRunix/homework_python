import random
import string
s = string.ascii_letters
n = ''
l = [c for c in s]
def cr_str(width):
    l = [random.choice(string.ascii_letters) for i in range(width)]
    s = ''
    for el in l:
        s += el
    return s
#print(cr_str(9))

def caps(f):
    b = 0
    m = 0
    for i in f:
        if i.isupper():
            m += 1
        else:
            b += 1
    if b > m:
        return 1
    elif m > b:
        return 0
    else:
        return -1
#print(cr_str(9), caps(cr_str(9)))

#      Homework
def cr_list_str(width, num):
    l = [cr_str(width) for i in range(num) ]
    s = ''
    big = 0
    small = 0
    statb = 0
    stats = 0
    statr = 0
    for el in l:
        s += el
        s += ' '
        for i in el:
            if i.isupper():
                big += 1
            else:
                small += 1
        if big > small:
            statb += 1
            s += '1'
        elif small > big:
            stats += 1
            s += '0'
        else:
            statr += 1
            s += '-1'
        
        s += ' '
    s += '> A ' + str(statb/(statb+stats+statr)*100) + '% '
    s += '> a ' + str(stats/(statb+stats+statr)*100) + '% '
    s += 'a == A ' + str(statr/(statb+stats+statr)*100) + '%'
    return s

print(cr_list_str(8, 8),)