import csv
from sqlite3 import Row
from wsgiref import headers

dataSet1 = []
dataSet2 = []

with open ("final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataSet1.append(i)
with open ("data.csv", "r") as f:
    csv_reader2 = csv.reader(f)
    for i in csv_reader2:
        dataSet2.append(i)
# print(dataSet1)
headers1 = dataSet1[0]
headers2 = dataSet2[0]
planet_data1 = dataSet1[1:]
planet_data2 = dataSet2[1:]

headers = headers1+headers2
planet_data = []
for i,data in enumerate(planet_data1):
    planet_data.append(planet_data1[i]+planet_data2[i])

with open ("main.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)


















