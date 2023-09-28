from re import I


a = int(input())
if a > 0:
    c = 0
    i = 0
    for i in range(1,a+1):
        if a % i == 0:
            c = c + 1
    if c >= 3:
        print("not prime")
    else:
        print("prime")

    


    