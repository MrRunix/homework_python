import random
s = str(input())
def furmut(s):
    t = s.split('.')
    if len(t) < 2:
        return 'Invalid'
    else:
        return '.' + t[-1]
#print(furmut(s))

def time(c):
    return (str(c // 86400) + ':' + str(c % 86400 // 3600) + ':' + str(c % 86400 % 3600 // 60) + ':' + str(c % 86400 % 3600 % 60))
#print(time(666666))

def palindrome(s):
    if len(s) % 2 != 0:
        s.replace(s[len(s)//2+1],"")
    t = 0
    for i in range(len(s)//2):
        if s[i] == s[-i]:
            t += 1
        else:
            return False
            break
    if t == len(s) // 2:
        return True
#palindrome(s)        доработать(

def is_palindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False
#print(is_palindrom(s))

n = int(input())
def stranny_sum(n):
    return int(str(n)) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(stranny_sum(n))

def gen_list(num, mini, maxi):
    i = 0
    while i < num:
        yield random.randrange(mini, maxi)
        i += 1
