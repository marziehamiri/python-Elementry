my_list1 = []
my_list2 = []
n = int(input())
for i in range(n):
    my_str_i = input()
    my_list1 = my_str_i.split()

    for i in range(len(my_list1)):
        my_list1[i] = int(my_list1[i])

    my_list2 = my_list2.append(my_list1)
a = 0
c = 0
b = 0

for i in range(len(my_list2)):
    
    if a < my_list2[i][0] and b > my_list2[i][1]:
        c = c + 1
    if a > my_list2[i][0] and b < my_list2[i][1]:
        c = c + 1
    a = my_list2[i][0]
    b = my_list2[i][1]


if c >= 1 :
    print('happy irsa')
else:
    print('poor irsa')
    
        

    
            

    

    

