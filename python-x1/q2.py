# Q2(A)
def most_popular_chr(chrs_string):
    
    count_of_each_char = {}    
    order_of_chars = []
    
    ## loop through each character in the string
    for char in chrs_string:
        if char not in count_of_each_char:
            ## start counting from 1 if this the first time i see this character
            count_of_each_char[char] = 1
            ## appends char to the end of the list 
            order_of_chars.append(char)
        else:
            ## if i've already seen this character, I just add to its count.
            count_of_each_char[char] += 1
    
    ## find which character is the most common
    most_frequent_count = max(count_of_each_char.values())
    for char in order_of_chars:
        if count_of_each_char[char] == most_frequent_count:
            return char

## Tests
print(most_popular_chr("HelloWorld"))
print(most_popular_chr("aggcc cgbb"))


# -------------------- -------------------- -------------------- -------------------- 

## Q2(B)
def most_popular_digit(num):

    ## Convert num to str
    num_str = str(abs(num))
    ## Create dictionary
    count_digits = {}
    
    ## Go through each digit in the number and count it
    for digit in num_str:
        if digit in count_digits:
            count_digits[digit] += 1
        else:
            count_digits[digit] = 1
    
    ## Finds the digit that appeared the most times
    most_frequent = None
    max_count = 0
    for digit, count in count_digits.items():
        if count > max_count:
            max_count = count
            most_frequent = digit
    return int(most_frequent) # Convert to int before return

## Tests
print(most_popular_digit(12341))  # אמור להחזיר 1
print(most_popular_digit(-1223241))  # אמור להחזיר 2
