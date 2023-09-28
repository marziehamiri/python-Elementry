the_string = input()
x1, x2,x3 = the_string.split()

x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

if x1 < x2 < x3:
    print((x3 - x2)+(x2 - x1))
if x1 < x3 < x2:
    print((x2 - x3)+(x3 - x1))
if x2 < x1 < x3:
    print((x3 - x1)+(x1 - x2))
if x2 < x3 < x1:
    print((x1 - x3)+(x3 - x2))
if x3 < x1 < x2:
    print((x2 - x1)+(x1 - x3))
if x3 < x2 < x1:
    print((x1 - x2)+(x2 - x3))
    