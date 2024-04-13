## Q3(A)
def substrings_locations(chrs_string, k):
    ## empty dictionary
    substrings_dict = {}
    ## to start index of the substring
    start_index = 0
    
    ## loop through all substrings of length k
    while start_index <= len(chrs_string) - k:
        ## get a substring of length k from the current index
        current_substring = chrs_string[start_index:start_index+k]
        ## check if substring has found
        if current_substring not in substrings_dict:
            ## add new substrings with their index to the dictionary
            substrings_dict[current_substring] = [start_index]
        else:
            ## append the index to the existing substring's list
            substrings_dict[current_substring].append(start_index)
        ## increase the start_index
        start_index += 1
    ## return the dictionary of substrings and their indexes
    return substrings_dict

# Let's test the function with an example
# example_string = 'TTAATTAGGGGCGC'
# substring_length = 2
## Q3(A)
print(substrings_locations('TTAATTAGGGGCGC', 2))


## Q3(B)

def reverse_dict(d):
    ## empty dictionary
    reversed_mapping = {}
    ## get the list of keys
    list_of_keys = list(d.keys())
    
    ## get through each key
    for index in range(len(list_of_keys)):
        ## get the current key
        current_key = list_of_keys[index]
        ## matching the current key
        current_value_list = d[current_key]
        
        ## through each value
        for value_index in range(len(current_value_list)):
            ## get the current value
            current_value = current_value_list[value_index]
            ## checks if the current value exists
            if current_value not in reversed_mapping:
                ## creates a new list with the current key
                reversed_mapping[current_value] = [current_key]
            else:
                ## adds the current key to the list
                reversed_mapping[current_value].append(current_key)
    ## returns the reverse dictionary
    return reversed_mapping

# דוגמה לשימוש בפונקציה
# example_dict = {"aa": [1, 3, "b"], 555: [1, "jx"]}
## Q3(B)
print(reverse_dict({"aa": [1, 3, "b"], 555: [1, "jx"]}))
# תוצאה צפויה: {1: ['aa', 555], 3: ['aa'], 'b': ['aa'], 'jx': [555]}

