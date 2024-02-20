code = input()

i = 0
new_code = ''
while (i < len(code)):
    if code[i: i+2] == '--':
        new_code += '2'
        i += 1
    elif code[i: i+2] == '-.':
        new_code += '1'
        i += 1
    elif code[i] == '.':
        new_code += '0'
    i += 1
code = new_code
print(code)
