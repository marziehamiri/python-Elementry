mux1 = 0
mux2 = 0
age1 = int(input())
while age1 != -1 and 10 <= age1 <= 90:
    if age1 > mux1:
        mux2 = mux1
        mux1 = age1 
    if age1 < mux1 and age1 > mux2:
        mux2 = age1
    
    age1 = int(input())     
print(mux1," ",mux2)

