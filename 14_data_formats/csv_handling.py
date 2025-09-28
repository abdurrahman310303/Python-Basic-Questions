import csv
import io

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

people_dict = [
    {'Name': 'David', 'Age': 28, 'City': 'Boston'},
    {'Name': 'Eve', 'Age': 32, 'City': 'Seattle'},
    {'Name': 'Frank', 'Age': 29, 'City': 'Denver'}
]

with open('people_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people_dict)

csv_string = "Name,Score,Grade\nAlice,85,B\nBob,92,A\nCharlie,78,C"
reader = csv.reader(io.StringIO(csv_string))
for row in reader:
    print(row)
