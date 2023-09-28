import random
a = random.randint(1,100)
g = int(input("please enter a number: "))

while a!=g:
    if a > g:
        print("mine is larger!")
    else:
        print("mine is smaller!")
    
    g = int(input("please enter a number: "))

print("wooow!you win the game...")


