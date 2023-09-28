mux1 = 0
mux2 = 0
age3 = 0
age2 = 0
age1 = int(input())
while age1 != -1 and 10 <= age1 <= 90:
    if age1 > mux1:
        mux2 = mux1
        mux1 = age1
    age3 = age2   
    age2 = int(input())
    if age3 == age2 or age1 == age2:
        break
    else:
        age1 = age2
        
print(mux1," ",mux2)



