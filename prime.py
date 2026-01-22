def main():
    print("First n prime numbers")
    n = int(input("Enter n: "))
    print(prime(n))

def prime(n=5):
    result, num = [], 2
    while len(result) < n:
        if all(num % p != 0 for p in result):
            result.append(num)
        num += 1
    return result

if __name__ == "__main__":
    main()