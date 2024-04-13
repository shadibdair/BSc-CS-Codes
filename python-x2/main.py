def is_valid_integer_csv(file_name):
    try:
        ## open the file
        with open(file_name, 'r') as file:
            ## reading the lines from the file
            lines = file.readlines()

            ## assume that lines be same length
            len_expected = None

            for line in lines:
                ## separate the line
                values = line.strip().split(',')
                ## check each row contain לפחות one integer
                is_int = False
                for value in values:
                    ## check if value is num
                    if value.isdigit():
                        is_int = True
                        ## exit loop
                        break
                ## if not find a number
                if not is_int:
                    return False
                # check that values are int or na
                for value in values:
                    ## if  value is not a num or na
                    if not (value.isdigit() or value == "na"):
                        return False
                ## if length of the first row as the expected length for the other rows
                if len_expected is None:
                    ## length for the lines
                    len_expected = len(values)
                else:
                    ## if length of current line -> different
                    if len(values) != len_expected:
                        return False
                    
            ## if all pass means the fils is FINE 
            return True
    except:
        ## return false if the file not found
        return False



def city_group(citizens_file):
    family_city_dict_details = {}
    try:
        ## read file 
        with open(citizens_file, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                ## check if there are four fields and no empty fields
                if len(fields) != 4 or '' in fields:
                    raise ValueError("Invalid input file")
                ## add fields to variable
                first_name = fields[0]
                last_name = fields[1]
                phone_number = fields[2]
                city = fields[3]       
                ## check if the number phone correct
                if len(phone_number) != 9 or not phone_number.isdigit():
                    raise ValueError("Invalid input file")
                ## check if the city's name contains (letters and spaces) ONLY
                if not all(char.isalpha() or char.isspace() for char in city):
                    raise ValueError("Invalid input file")
                ## check if city not in family_city_dict_details
                if city not in family_city_dict_details:
                    family_city_dict_details[city] = {}
                ## check if last_name not in family_city_dict_details
                if last_name not in family_city_dict_details[city]:
                    family_city_dict_details[city][last_name] = 1
                else:
                    family_city_dict_details[city][last_name] += 1

    except IOError:
        return {}
    return family_city_dict_details


def connected_nodes(graph, node):
    ## list nodes visited
    visited = []
    ## list nodes need to check
    explore = [node]
    ## while stil there nodes for check
    while explore:
        ## it take the first node from explore list
        current_node = explore.pop(0)
        if current_node not in visited:
            ## add current node to visited list
            visited.append(current_node)
            ## check if current node has nearbys
            if current_node in graph:
                ## get list of nearbys for current node
                nearbys = graph[current_node]
                ## loop for the nearbys
                for nearby in nearbys:
                    ## will only add the nearby if not already in visited or explore lists
                    if nearby not in visited and nearby not in explore:
                        ## will add nearby to explore list
                        explore.append(nearby)

    return visited



def coalition(votes, n):
    ## empty list
    coalitions = [[]]
    ## loop to each candidate and their votes
    for candidate, votes_received in votes:
        ## list to store updated coalitions
        new_coalitions = []
        ## add current candidate to exist coalitions
        for exist_coalition in coalitions:
            new_coalition = exist_coalition + [(candidate, votes_received)]
            new_coalitions.append(new_coalition)
        ## update main list
        coalitions.extend(new_coalitions)
    ## check if any coalition has exactly n votes
    for coalition in coalitions:
        ## calculate total votes for coalition in basic way
        total_votes = 0
        ## use more variable name
        for candidate_details in coalition:
            ## access votes directly via index
            candidate_votes = candidate_details[1]
            total_votes += candidate_votes
        if total_votes == n:
            ## found coalition with exactly n votes
            return True
    return False

