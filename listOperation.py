evens = list(range(2,22,2))

print(evens)

evens.insert(0,0)
print(evens)

evens.append(22)
print(evens)

evens.remove(22)
print(evens)

print(evens[0])
print(evens[-1])
print(evens[3:7])

for num in evens:
    print(num, end=" ")

print()