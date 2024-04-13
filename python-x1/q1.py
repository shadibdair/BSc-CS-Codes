# Q1
def is_plus_minus_balanced(s):

    plus_count = 0
    minus_count = 0
    
    ## loop that check if string has only + or -
    for char in s:
        if char == '+':
            plus_count += 1
        elif char == '-':
            minus_count += 1
        else:
            return False ## invalid char
        
        if minus_count > plus_count:
            return False
    return plus_count == minus_count  ## plus and minus are equal ?

## Q1 Tests
print(is_plus_minus_balanced(""))
print(is_plus_minus_balanced("+-+"))
print(is_plus_minus_balanced("+-+-+-+-"))

