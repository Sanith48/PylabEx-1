def extract_last_characters(tpl):
    last_characters = []
    
    for string in tpl:
        last_characters.append(string[-1])
    
    return last_characters

input_tuple = ("python", "learn", "includehelp")

result = extract_last_characters(input_tuple)

print(result)
