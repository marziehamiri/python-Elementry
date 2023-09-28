def maghsoomalayh(a):
    i = 0
    c = 0
    for i in range(1,a+1):
        if a % i == 0:
            c = c + 1
    return c

print(maghsoomalayh(20))
