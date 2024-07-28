A = ['abc', 'xyz', 'aba', '1221']

# Iterate over the list with index
for index, string in enumerate(A):
    if len(string) > 0 and string[0] == string[-1]:
        print(f"String '{string}' at index {index} starts and ends with the same character.")
