num = 7
if (num % 2 == 0):
    print(f"{num} is even")
elif (num % 3 == 0):
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is odd and not divisible by 3")

for i in range(1, 6):
    print(i, end=" ")
print()

count = 6
while count > 0:
    print(count, end=" ")
    count -= 1
print()

print("----------------------")
print("Here's the pyramid:")

for i in range(1, 16):
    for i in range (0, i):
        print("*", end="")
    print()