def main():
    print("This is the entry point of the method")
    fibonacci(int(input("Enter number of elements: ")))

def fibonacci(n):
    previous=0
    next=1
    print(f"{previous} {next} ", end="")
    for i in range(1, n):
        num = previous + next
        print(f"{num}", end=" ")
        previous = next
        next = num
    print()

if __name__ == "__main__":
    main()
