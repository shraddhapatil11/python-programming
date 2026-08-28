# Generate Fibonacci series

terms = int(input("Enter the number of terms: "))

a = 0
b = 1

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci series:")

    for i in range(terms):
        print(a, end=" ")

        a, b = b, a + b
