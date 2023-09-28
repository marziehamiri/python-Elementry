Marks = {}
Marks = {"Marzieh":20,"Ali":18}
Marks["Marzieh"] = 19
print(Marks)
print(list(Marks.keys()))
if "Maryam" in Marks:
    print("True")
else:
    print("False")
str1 = "this is Marzieh"
for letter in str1:
    if letter in Marks:
        Marks[letter] += 1
    else:
        Marks[letter] = 1
print(Marks) 

