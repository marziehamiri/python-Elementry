a = input()
if "AB" and "BA" in a:
    a = a.replace("AB","XX",1)
    if "BA" in a:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
