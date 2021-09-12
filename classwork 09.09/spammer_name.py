import random
while True:
    def spammer(x):
        i = random.randint(1,100)
        return x*i
    name = input('введите имя')
    print(spammer(name))