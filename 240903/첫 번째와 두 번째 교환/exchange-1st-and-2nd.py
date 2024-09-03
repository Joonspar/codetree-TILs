def swap_chars(s):
    first_char = s[0]
    second_char = s[1]
    
    result = ''
    for char in s:
        if char == first_char:
            result += second_char
        elif char == second_char:
            result += first_char
        else:
            result += char
    
    return result
s = input()
print(swap_chars(s))