a = input()
C = 0
c = 0
for letter in a:
    if letter.islower():
        c = c+1
    else:
        C = C+1
if c < C:
    a = a.upper()
else:
    a = a.lower()
print(a)