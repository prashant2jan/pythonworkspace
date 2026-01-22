previous=0
next=1
n = int(input())
print(f"{previous} {next} ", end="")
for i in range(1, n):
    num = previous + next
    print(f"{num}", end=" ")
    previous = next
    next = num
print()