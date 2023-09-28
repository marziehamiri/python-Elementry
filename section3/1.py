a = input()

if "a" in a:
    a = a.replace("a","")
if "e" in a:
    a = a.replace("e","")
if "i" in a:
    a = a.replace("i","")
if "o" in a:
    a = a.replace("o","")
if "u" in a:
    a = a.replace("u","")
if "A" in a:
    a = a.replace("A","")
if "E" in a:
    a = a.replace("E","")
if "I" in a:
    a = a.replace("I","")
if "O" in a:
    a = a.replace("O","")
if "U" in a:
    a = a.replace("U","")

b = ""
for letter in a:
    letter = '.' + letter
    b = b + letter
a = b    
a = a.lower()           
print(a)  



