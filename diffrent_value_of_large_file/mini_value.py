import csv

with open("employees-1000.csv", "r") as file:
    reader = csv.DictReader(file)

    salaries = [int(row["salary"]) for row in reader]

print("Minimum salary:", min(salaries))
