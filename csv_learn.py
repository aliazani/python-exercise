import csv

with open('grade.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

# import csv
# f = open('C:\\Users\\Aliaz\\Desktop\\py\\grade.csv', 'r')
# reader = csv.reader(f)

# for row in reader :
#     print (row)


# sha256
# 0000 ---> 9999
# form i in range (0000 , 9999)

# import hashlib
# hashlib.sha256
