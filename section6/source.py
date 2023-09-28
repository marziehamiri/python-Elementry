import hashlib
import csv
import collections

def hash_password_hack(input_file_name, output_file_name):
    my_list = []
    f = open(input_file_name)
    reader = csv.reader(f)
    r = open(output_file_name,"w") 
    for i in range(1000,10000):
        i = str(i)
        encoded = i.encode()
        result = hashlib.sha256(encoded)
        result = result.hexdigest()
        res_dct = [result, i]
        my_list.append(res_dct)

    res_dct1 = collections.OrderedDict()
    def Convert(my_list): 
        res_dct1 = {my_list[i][0]: my_list[i][1] for i in range(0, len(my_list))}
        return res_dct1
    my_dic = collections.OrderedDict()
    my_dic = Convert(my_list)
       
    for row in reader:
        if row[1] in my_dic:
            a = row[1]
            r.write("{0},{1}\n".format(row[0],my_dic[a]))
        
#hash_password_hack("a.csv", "b.csv")       




    
    
    


