a = input()
if len(a) % 2 == 0:
    b = len(a)//2
    c = a[:b]
    d = a[:b-1:-1]
    if c == d:
        print("palindrome")
    else:
        print("not palindrome")
else:
    b = len(a)//2
    c = a[:b]
    d = a[:b:-1]
    if c == d:
        print("palindrome")
    else:
        print("not palindrome")
    
