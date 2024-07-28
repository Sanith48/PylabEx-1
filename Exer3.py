# Function to print the first pattern
def print_pattern_1():
    n = 5  # Number of rows
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print characters
        for j in range(i + 1):
            print(chr(65 + j), end=' ')
        print()

# Function to print the second pattern
def print_pattern_2():
    n = 5  # Number of rows
    for i in range(n):
        # Print stars
        print('* ' * (i + 1))

# Print the patterns
print("Pattern 1:")
print_pattern_1()
print("\nPattern 2:")
print_pattern_2()
