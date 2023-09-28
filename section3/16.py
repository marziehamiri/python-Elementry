import math
my_list = []
my_str = ''
n = int(input())
for i in range(n):
    my_list.append(int(input()))
for i in range(len(my_list)):
    my_list[i] = math.sqrt(my_list[i])
    my_str ='%.8f'%(my_list[i])
    my_str = my_str[:-4]
    print(my_str)

 
   
