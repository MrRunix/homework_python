import random
while True:
    def gl(x):
        i = random.randint(100,700)
        return x*i
    name = input('введите имя')
    print(gl(name))