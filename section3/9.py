
n = int(input())
count = 0
the_string = input()
my_list=the_string.split()
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
    if my_list[i] <= 2 :
        count = count + 1
print(count // 3)
        




