## Q1
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

## Q2(A)
def most_popular_chr(chrs_string):
    count_char = {}    
    order_chars = []
    
    ## loop through each character in the string
    for char in chrs_string:
        if char not in count_char:
            ## start counting from 1 if this the first time i see this character
            count_char[char] = 1
            ## appends char to the end of the list 
            order_chars.append(char)
        else:
            ## if i've already seen this character, I just add to its count
            count_char[char] += 1
    
    ## find which character is the most common
    most_frequent_count = max(count_char.values())
    for char in order_chars:
        if count_char[char] == most_frequent_count:
            return char


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


## Q3(A)
def substrings_locations(chrs_string, k):
    ## empty dictionary
    dict_substrings = {}
    ## to start index of the substring
    start_index = 0
    
    ## loop through all substrings of length k
    while start_index <= len(chrs_string) - k:
        ## get a substring of length k from the current index
        current_substring = chrs_string[start_index:start_index+k]
        ## check if substring has found
        if current_substring not in dict_substrings:
            ## add new substrings with their index to the dictionary
            dict_substrings[current_substring] = [start_index]
        else:
            ## append the index to the existing substring's list
            dict_substrings[current_substring].append(start_index)
        ## increase the start_index
        start_index += 1
    ## return the dictionary of substrings and their indexes
    return dict_substrings


## Q3(B)
def reverse_dict(d):
    ## empty dictionary
    reverse_mapping = {}
    ## get the list of keys
    list_keys = list(d.keys())
    
    ## get through each key
    for index in range(len(list_keys)):
        ## get the current key
        current_key = list_keys[index]
        ## matching the current key
        current_list = d[current_key]
        
        ## through each value
        for value_index in range(len(current_list)):
            ## get the current value
            current_value = current_list[value_index]
            ## checks if the current value exists
            if current_value not in reverse_mapping:
                ## creates a new list with the current key
                reverse_mapping[current_value] = [current_key]
            else:
                ## adds the current key to the list
                reverse_mapping[current_value].append(current_key)
    ## returns the reverse dictionary
    return reverse_mapping


## Q4(A)
def mat_from_list_to_dict(mat_list):
    ## empty dictionary
    dict_matrix = {}
    
    # loop over rows of matrix
    for row_index in range(len(mat_list)):
        # loop over each element in row.
        for col_index in range(len(mat_list[row_index])):
            key = (row_index + 1, col_index + 1)
            value = mat_list[row_index][col_index]
            # add to dictionary
            dict_matrix[key] = value    
    return dict_matrix


## Q4(B)
def mat_from_dict_to_list(mat_dict):
    # find matrix size
    max_row = 0
    max_col = 0
    for key in mat_dict.keys():
        if key[0] > max_row:
            max_row = key[0]
        if key[1] > max_col:
            max_col = key[1]
    
    ## empty list
    list__matrix = []
    for i in range(max_row):
        row = []
        for j in range(max_col):
            row.append(0)  ## fill zeros 
        list__matrix.append(row)
    
    ## fill matrix with values from dict
    for key, value in mat_dict.items():
        row_index = key[0] - 1
        col_index = key[1] - 1
        list__matrix[row_index][col_index] = value
    return list__matrix


## Q4(C)
def mat_transpose(A):
    ## if A is list
    if isinstance(A, list):
        ## create new matrix
        transpose = []
        ## loop over columns
        for i in range(len(A[0])):
            new_row = []
            ## loop over rows
            for row in A:
                new_row.append(row[i])
            transpose.append(new_row)
        return transpose
    
    ## if A is dictionary
    elif isinstance(A, dict):
        dict_transpose = {}
        ## loop max row and col calc
        max_row = 0
        max_col = 0
        for key in A.keys():
            if key[0] > max_row:
                max_row = key[0]
            if key[1] > max_col:
                max_col = key[1]
        
        ## swap row and column indices
        for i in range(1, max_row + 1):
            for j in range(1, max_col + 1):
                if (i, j) in A:
                    dict_transpose[(j, i)] = A[(i, j)]
        return dict_transpose


## Q4(D)
def mult_with_transpose(A):
    ## if A is list
    if isinstance(A, list):
        ## initialize matrix
        result = []
        ## loop over rows of A
        for i in range(len(A)):
            row_result = []
            ## loop over columns of A
            for j in range(len(A)):
                sum = 0
                ## multiplication
                for k in range(len(A[0])):
                    if j < len(A) and k < len(A[0]):
                        sum += A[i][k] * A[j][k]
                row_result.append(sum)
            result.append(row_result)
        return result

    ## if A is dictionary
    elif isinstance(A, dict):
        ## initialize dictionary
        result = {}
        ## size of the matrix
        size = max(max(key) for key in A.keys())
        ## loop over rows
        for i in range(1, size + 1):
            ## loop over columns
            for j in range(1, size + 1):
                sum = 0
                ## multiplication
                for k in range(1, size + 1):
                    sum += A.get((i, k), 0) * A.get((j, k), 0)
                result[(i, j)] = sum
        return result