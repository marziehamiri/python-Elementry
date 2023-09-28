import collections

n = int(input())
countries = []
for i in range(n):
    countries.append(input())
my_dic = collections.OrderedDict()
for country in countries:
    my_dic[country] = my_dic.get(country,0) + 1
for x, y in sorted(my_dic.items()):
      print(x, y)


     
