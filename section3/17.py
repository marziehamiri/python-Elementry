f = open('1.txt')
counter = 0
f.readline()
'''for line in f:
    counter +=1
    print("line number %i is : %s " %(counter,line))'''
'''for line in f:
    print(line.strip())'''
sum = counter = 0
for line in f:
    counter += 1
    this_number = int(line.strip())
    sum = sum + this_number
print(sum)
mak= open('mak.txt')
print(type(mak.readlines()))
print(type(mak.read()))
print(type(mak.readline()))


