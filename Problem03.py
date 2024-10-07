s = input("Enter a string: ")
digit_count = sum(c.isdigit() for c in s)
print(f"Total digits are: {digit_count}")