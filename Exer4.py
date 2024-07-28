# Given lists
ListColourNames = ["Black", "Red", "Maroon", "Yellow"]
ListColourCodes = ["000000", "FF0000", "800000", "FFFF00"]

# Combine the lists into a list of dictionaries
list_of_dicts = [
    {"colorName": name, "colorCode": code}
    for name, code in zip(ListColourNames, ListColourCodes)
]

# Print the result
for color_dict in list_of_dicts:
    print(color_dict)
