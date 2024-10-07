def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two numbers."

    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return "There is no second largest number, all numbers are the same."
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Second largest number:", find_second_largest(numbers))