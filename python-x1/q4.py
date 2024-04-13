## Q4(A)
def mat_from_list_to_dict(mat_list):
    ## empty dictionary
    matrix_as_dict = {}
    
    # loop over rows of matrix
    for row_index in range(len(mat_list)):
        # loop over each element in row.
        for col_index in range(len(mat_list[row_index])):
            key = (row_index + 1, col_index + 1)
            value = mat_list[row_index][col_index]
            # add to dictionary
            matrix_as_dict[key] = value    
    return matrix_as_dict

## Test
## Q4(A)
print(mat_from_list_to_dict([[1, 2], [3, 4], [5, 6]]))
# Expected output: {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4, (3, 1): 5, (3, 2): 6}

# ------------------- ------------------- ------------------- -------------------

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
    matrix_list = []
    for i in range(max_row):
        row = []
        for j in range(max_col):
            row.append(0)  ## fill zeros 
        matrix_list.append(row)
    
    ## fill matrix with values from dict
    for key, value in mat_dict.items():
        row_index = key[0] - 1
        col_index = key[1] - 1
        matrix_list[row_index][col_index] = value
    return matrix_list

## Test
## Q4(B)
mat_dict_example = {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4, (3, 1): 5, (3, 2): 6}
print(mat_from_dict_to_list(mat_dict_example))
# Expected output: [[1, 2], [3, 4], [5, 6]]

# ------------------- ------------------- ------------------- -------------------

## Q4(C)
def mat_transpose(A):
    ## if A is list
    if isinstance(A, list):
        ## create new matrix
        transposed = []
        ## loop over columns
        for i in range(len(A[0])):
            new_row = []
            ## loop over rows
            for row in A:
                new_row.append(row[i])
            transposed.append(new_row)
        return transposed
    
    ## if A is dictionary
    elif isinstance(A, dict):
        transposed_dict = {}
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
                    transposed_dict[(j, i)] = A[(i, j)]
        return transposed_dict


## Q4(C)
print(mat_transpose([[1, 2], [3, 4], [5, 6]]))  # For nested list
# Expected to return [[1, 3, 5], [2, 4, 6]]

print(mat_transpose({(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4, (3, 1): 5, (3, 2): 6}))  # For dictionary
# Expected to return {(1, 1): 1, (2, 1): 2, (1, 2): 3, (2, 2): 4, (1, 3): 5, (2, 3): 6}


# ------------------- ------------------- ------------------- -------------------

## Q4(D)
def mult_with_transpose(A):
    ## if A is list
    if isinstance(A, list):
        ## initialize matrix
        result = []
        ## loop over rows of A
        for i in range(len(A)):
            result_row = []
            ## loop over columns of A
            for j in range(len(A)):
                sum_product = 0
                ## multiplication
                for k in range(len(A[0])):
                    if j < len(A) and k < len(A[0]):
                        sum_product += A[i][k] * A[j][k]
                result_row.append(sum_product)
            result.append(result_row)
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
                sum_product = 0
                ## multiplication
                for k in range(1, size + 1):
                    sum_product += A.get((i, k), 0) * A.get((j, k), 0)
                result[(i, j)] = sum_product
        return result

# Testing the function
## Q4(D)
print(mult_with_transpose([[1, 2], [3, 4], [5, 6]]))
# Expected: [[5, 11, 17], [11, 25, 39], [17, 39, 61]]

print(mult_with_transpose({(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4, (3, 1): 5, (3, 2): 6}))
# Expected: {(1, 1): 5, (1, 2): 11, (1, 3): 17, (2, 1): 11, (2, 2): 25, (2, 3): 39, (3, 1): 17, (3, 2): 39, (3, 3): 61}
