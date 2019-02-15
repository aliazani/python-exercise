import csv

file = open("C:\\Users\\Aliaz\\Desktop\\py\\tech.csv", mode='w', newline="")
field = ['name', 'family', 'topic']
data = csv.DictWriter(file, fieldnames=field)
data.writeheader()

data.writerow({'name': 'ali',
               'family': 'azani',
               'topic': 'learn'})
data.writerow({'name': 'mohsen',
               'family': 'beyrami',
               'topic': 'play'})
