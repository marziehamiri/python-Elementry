from ast import operator
import csv
from collections import OrderedDict
# For the average
from statistics import mean
import statistics 
from operator import itemgetter


def calculate_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    reader = csv.reader(f)
    r = open(output_file_name,"w") 
    for row in reader:
        name = row[0]
        these_grades = []
        for grade in row[1:]:
            these_grades.append(float(grade))
        
        #r.write("%s,%f\n"%(name,statistics.mean(these_grades)))
        r.write('{0},{1}\n'.format(name,statistics.mean(these_grades)))

    
            
def calculate_sorted_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    reader = csv.reader(f)
    r = open(output_file_name,"w") 
    my_list2 = []
    for row in reader:
        these_grades = []
        name = row[0]
        for grade in row[1:]:
            these_grades.append(float(grade))
        #my_string = "%s %f"%(name,statistics.mean(these_grades))
        my_string ='{0} {1}\n'.format(name,statistics.mean(these_grades))
        my_list1 = my_string.split()
        my_list2.append(my_list1)
    def Convert(my_list2):
        res_dct = OrderedDict()
        res_dct = {my_list2[i][0]: float(my_list2[i][1]) for i in range(0, len(my_list2))}
        return res_dct
    my_dic = Convert(my_list2)
    marklist = sorted(my_dic.items(), key=lambda x:x[1])
    
    _before = 0
    for i in range(len(marklist)):
        if float(marklist[i][1]) != _before:
            _before = float(marklist[i][1])
            num2 = i
            num3 = num2   
        else:
            num2 = i
            marklist1 = sorted([marklist[num2],marklist[num3]],key =lambda x:x[0] )
            marklist[num3],marklist[num2] = marklist1
    

    for i in range(len(marklist)):
        #"%s,%s\n"%(marklist[i][0],marklist[i][1])
        r.write('{0},{1}\n'.format(marklist[i][0],marklist[i][1]))
        

def calculate_three_best(input_file_name, output_file_name):
    f = open(input_file_name)
    reader = csv.reader(f)
    r = open(output_file_name,"w") 
    my_list2 = []
    my_list3 = []
    for row in reader:
        these_grades = []
        name = row[0]
        for grade in row[1:]:
            these_grades.append(float(grade))
        #my_string = "%s %f"%(name,statistics.mean(these_grades))
        my_string ='{0} {1}\n'.format(name,statistics.mean(these_grades))
        my_list1 = my_string.split()
        my_list2.append(my_list1)
    def find_mux1():
        mux1 = 0
        for i in range(len(my_list2)):
            
            if float(my_list2[i][1]) > mux1:
                mux1 = float(my_list2[i][1])
                mux_name = my_list2[i][0]
                mux_num = i
            elif float(my_list2[i][1]) == mux1:
                mux1 = float(my_list2[i][1])
                mux_name = my_list2[i][0]
                mux_num = i
                mux_num_before = i - 1
                my_list2_1 = sorted([my_list2[mux_num],my_list2[mux_num_before]],key =lambda x:x[0] )
                my_list2[mux_num],my_list2[mux_num_before] = my_list2_1

        return mux1,mux_name,mux_num
            
    mux1,mux_name,mux_num = find_mux1()
    my_list2.remove(my_list2[mux_num])
    my_list3.append("{0},{1}".format(mux_name,mux1))
    def find_mux2():
        mux2 = 0
        for i in range(len(my_list2)):
            
            if float(my_list2[i][1]) > mux2:
                mux2 = float(my_list2[i][1])
                mux2_name = my_list2[i][0]
                mux2_num = i
            elif float(my_list2[i][1]) == mux2:
                mux2 = float(my_list2[i][1])
                mux2_name = my_list2[i][0]
                mux2_num = i
                mux2_num_before = i - 1
                my_list2_2 = sorted([my_list2[mux2_num],my_list2[mux2_num_before]],key =lambda x:x[0] )
                my_list2[mux2_num],my_list2[mux2_num_before] = my_list2_2


        return mux2,mux2_name,mux2_num
    mux2,mux2_name,mux2_num = find_mux2()
    my_list2.remove(my_list2[mux2_num])
    my_list3.append("%s,%f"%(mux2_name,mux2))
    def find_mux3():
        mux3 = 0
        for i in range(len(my_list2)):
            
            if float(my_list2[i][1]) > mux3:
                mux3 = float(my_list2[i][1])
                mux3_name = my_list2[i][0]
                mux3_num = i
            elif float(my_list2[i][1]) == mux3:
                mux3 = float(my_list2[i][1])
                mux3_name = my_list2[i][0]
                mux3_num = i
                mux3_num_before = i - 1
                my_list2_3 = sorted([my_list2[mux3_num],my_list2[mux3_num_before]],key =lambda x:x[0] )
                my_list2[mux3_num],my_list2[mux3_num_before] = my_list2_3


                
        return mux3,mux3_name,mux3_num
    mux3,mux3_name,mux3_num = find_mux3()
    my_list2.remove(my_list2[mux3_num])
    my_list3.append("{0},{1}".format(mux3_name,mux3))
    for i in range(len(my_list3)):
        r.write(my_list3[i])
        r.write("\n")


def calculate_three_worst(input_file_name, output_file_name):
    f = open(input_file_name)
    reader = csv.reader(f)
    r = open(output_file_name,"w") 
    my_list2 = []
    my_list3 = []
    my_list4 = []
    for row in reader:
        these_grades = []
        name = row[0]
        for grade in row[1:]:
            these_grades.append(float(grade))
        my_string = "%s %0.15f"%(name,statistics.mean(these_grades))
        my_list1 = my_string.split()
        my_list2.append(my_list1)
    def find_mux1():
        mux1 = 0
        for i in range(len(my_list2)):
            
            if float(my_list2[i][1]) > mux1:
                mux1 = float(my_list2[i][1])
                mux_name = my_list2[i][0]
                mux_num = i
        return mux1,mux_name,mux_num
            
    mux1,mux_name,mux_num = find_mux1()
    my_list2.remove(my_list2[mux_num])
    my_list3.append("%s,%f"%(mux_name,mux1))
    def find_mux2():
        mux2 = 0
        for i in range(len(my_list2)):
            
            if float(my_list2[i][1]) > mux2:
                mux2 = float(my_list2[i][1])
                mux2_name = my_list2[i][0]
                mux2_num = i
        return mux2,mux2_name,mux2_num
    mux2,mux2_name,mux2_num = find_mux2()
    my_list2.remove(my_list2[mux2_num])
    my_list3.append("%s,%f"%(mux2_name,mux2))
    def find_mux3():
        mux3 = 0
        for i in range(len(my_list2)):
            
            if float(my_list2[i][1]) > mux3:
                mux3 = float(my_list2[i][1])
                mux3_name = my_list2[i][0]
                mux3_num = i
        return mux3,mux3_name,mux3_num
    mux3,mux3_name,mux3_num = find_mux3()
    my_list2.remove(my_list2[mux3_num])
    my_list3.append("%s,%f"%(mux3_name,mux3))
    def find_min1():
        min1 = 0
        for i in range(len(my_list2)):
            if i == 0:
                min1 = float(my_list2[i][1])
                min1_num = i
            else:
                if float(my_list2[i][1]) < min1:
                    min1 = float(my_list2[i][1])
                    min1_num = i    
        return min1,min1_num
    min1,min1_num = find_min1()
    my_list2.remove(my_list2[min1_num])
    my_list4.append(min1)
    def find_min2():
        min2 = 0
        for i in range(len(my_list2)):
            if i == 0:
                min2 = float(my_list2[i][1])
                min2_num = i
            else:
                if float(my_list2[i][1]) < min2:
                    min2 = float(my_list2[i][1])
                    min2_num = i    
        return min2,min2_num
    min2,min2_num = find_min2()
    my_list2.remove(my_list2[min2_num])
    my_list4.append(min2)
    def find_min3():
        min3 = 0
        for i in range(len(my_list2)):
            if i == 0:
                min3 = float(my_list2[i][1])
                min3_num = i
            else:
                if float(my_list2[i][1]) < min3:
                    min3 = float(my_list2[i][1])
                    min3_num = i    
        return min3,min3_num
    min3,min3_num = find_min3()
    my_list2.remove(my_list2[min3_num])
    my_list4.append(min3)
    for i in range(len(my_list4)):
        r.write(str(my_list4[i]))
        r.write("\n")

def calculate_average_of_averages(input_file_name, output_file_name):
    f = open(input_file_name)
    reader = csv.reader(f)
    r = open(output_file_name,"w") 
    my_list2 = []
    my_list5 = []
    for row in reader:
        these_grades = []
        name = row[0]
        for grade in row[1:]:
            these_grades.append(float(grade))
        my_string = "%s %0.15f"%(name,statistics.mean(these_grades))
        my_list1 = my_string.split()
        my_list2.append(my_list1)
    for i in range(len(my_list2)):
        my_list5.append(float(my_list2[i][1]))
    r.write("%0.15f"%(statistics.mean(my_list5)))

    






#calculate_averages("grades1.csv", "result1.csv")
calculate_sorted_averages("grades1.csv", "result1.csv")
#calculate_three_best("grades1.csv", "result1.csv")
#calculate_three_worst("grades1.csv", "result1.csv")
#calculate_average_of_averages("grades1.csv", "result1.csv")