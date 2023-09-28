def maghsoomalayh(a):
    i = 0
    c = 0
    for i in range(1,a+1):
        if a % i == 0:
            c = c + 1
    return c

muxC = 0
muxCa = 0 



for i in range(0,20):

    a = int(input())
    C = maghsoomalayh(a)
    
    if C > muxC:
        muxC = C
        muxCa = a
    if C == muxC and a > muxCa:
        muxCa = a
    


print(muxCa," ",muxC)









