
mux = 0
age = int(input())
while age != -1 and 10 <= age <= 90:
    if age > mux:
        mux = age
    age = int(input())
        
print(mux)




