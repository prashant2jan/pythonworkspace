import csv

data = [
    ["Tom", "Dick", "Harry"],
    ["Alice", "in", 1, "der", "land"],
    ["One", 2, 3, "Four"]
]

with open("people.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)