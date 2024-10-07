def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Vowels (both lowercase and uppercase)
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count
input_string =input("Enter any String:")
print(f"Number of vowels: {count_vowels(input_string)}")