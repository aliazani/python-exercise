import csv

with open('C:\\Users\\Aliaz\\Desktop\\py\\tech.csv', newline='') as csv_file:
    spam_reader = csv.reader(csv_file)
    for row in spam_reader:
        print(', '.join(row))
