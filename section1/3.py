a = input()
x = len(a)
if x == 3:
    a = int(a)
    b1 = a // 10
    a3 = a % 10
    b2 = b1 // 10
    a2 = b1 % 10
    b3 = b2 // 10
    a1 = b2 % 10
    if (b3 == 0):
        a = a3 * 100 + a2 * 10 + a1 
        a = a * 2


        print(a)


    