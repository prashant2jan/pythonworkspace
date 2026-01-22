primes = {2, 3, 5, 7}
primes.add(11)
print(11 in primes)                # True
print(primes <= {2, 3, 5, 7, 11})  # True

# Set operations
evens = {2, 4, 6, 8}
odd = {1, 3, 5, 7}
print(primes & evens)               # {}
print(primes | evens)               # {2, 3, 4, 5, 6, 7, 8, 11}
print(primes - evens)               # {3, 5, 7, 11}
print(primes ^ evens)               # {2, 3, 4, 5, 6, 7, 8, 11}