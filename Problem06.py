def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a =int(input("Enter first Number:"))
b =int(input("Enter second Number:"))
print(f"GCD of {a} and {b} is: {gcd(a, b)}")