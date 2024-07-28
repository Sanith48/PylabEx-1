def print_even_numbers_and_squares(start, end):
    print(f"Even numbers and their squares in the range {start} to {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Even number: {num}, Square: {num ** 2}")

# Range (1, 50)
print_even_numbers_and_squares(1, 50)

print("\n")  # Print a newline for separation

# Range (1, 100)
print_even_numbers_and_squares(1, 100)
