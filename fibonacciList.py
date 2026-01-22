previous = 0
next = 1
n = 10
fiboList = list(range(previous, next+1, 1))
for i in range(1, n):
    num = previous + next
    fiboList.append(num)
    previous = next
    next = num
print(f"Fibonacci as list is: {fiboList}")