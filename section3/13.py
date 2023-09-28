import collections

my_dic = collections.OrderedDict()
n = int(input())
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
string2 = ""
for i in range(n):
    str1 = input()
    my_list1 = str1.split()
    my_list2.append(my_list1)

str2 = input()
my_list4 = str2.split()


def Convert(my_list2):
    res_dct = {my_list2[i][0]: my_list2[i][1] for i in range(0, len(my_list2))}
    return res_dct

my_dic = Convert(my_list2)
for word in my_list4:
    if word in my_dic:
        my_list3.append(my_dic[word])
    else:
        my_list3.append(word)
for i in my_list3:
       string2=string2+i+" "

print(string2)






    
    
    
