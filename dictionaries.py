student_grades = {
    "Alice" : 92,
    "Bob" : 87,
    "Sandy" : 78
 }

print(student_grades["Sandy"])

student_grades["Alice"] = 94
student_grades["Charlie"] = 98

for name, grades in student_grades.items():
    print(f"{name} {grades}")

print(student_grades.get("Eva", "Not Found"))
print(list(student_grades.keys()))
print(list(student_grades.values()))