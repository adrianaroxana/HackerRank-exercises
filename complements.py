def dnaComplement(str):
    # Write your code here
    
    reversedstring = reversed(str)
    output = ''
    for letter in reversedstring:
        letter = letter.upper()
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'
    return output


str = input("Insert your string")
print(dnaComplement(str))