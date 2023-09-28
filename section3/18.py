import csv
import statistics
f = open("grades.csv")
reader = csv.reader(f)
for row in reader:
    #print(row)
    name = row[0]
    these_grades = []
    for grade in row[1:]:
        these_grades.append(int(grade))
    print("average of %s is %f"%(name,statistics.mean(these_grades)))



