import random
a = 1
b = 99
guess = random.randint(a,b)
print(guess)
javab = input("Enter your idea: ")


while javab!="d":
    if javab == "b":
        #print("Please enter a larger number!")
        a = guess
        guess = random.randint(a,b)
        print(guess)
        javab = input("Enter your idea: ")


    elif javab == "k":
        #print("Please enter a smaller number!")
        b = guess
        guess = random.randint(a,b)
        print(guess)
        javab = input("Enter your idea: ")

print("you gess correctly!")

