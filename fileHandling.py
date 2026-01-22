with open("example.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print(contents)

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("example12\n")
    file.write("example13")

with open("example.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print(contents)

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("example1\n")
    file.write("example2\n")
    file.write("example3\n")
    file.write("example4\n")
    file.write("example5\n")
    file.write("example6\n")
    file.write("example7\n")
    file.write("example8\n")
    file.write("example9\n")
    file.write("example10\n")
    file.write("example11\n")
    file.write("example12\n")
    file.write("example13\n")
    file.write("example14\n")

with open("example.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print(contents)